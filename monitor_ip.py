#在互联网攻击日益增多的当下， 如何做好防护使我们日益需要关注的
#例如在ssh暴露在公网上时，不停地会有黑客的嗅探，不看日志不知道，一看吓一跳
#网上也有类似的防护工具，例如denyhost, 发现可疑ip后加入host.denny文件中
#我写这个功能类似，发现可疑IP后，加入iptables黑名单， 若干时间后解除
#相比denyhost好处是可定制化程度更高， 不限于ssh协议，无论什么日志，只要设定好相关的error关键词，能够获取IP，就能实现阻塞攻击的目的
#大致原理是读取日志，把当前日志行数记录下来,后面再读日志文件时，就能获取差异，也就是新增日志文件，在新增的日志文件里，通过自定义关键词查找锁定ip
#然后通过iptables锁定IP
#运行环境python3   执行方法python3 monitor_ip.py  可以尝试加入开机任务rc.local文件中
#主要需要要修改的是action中log路径，日志中关键词的定义，以及对ip抓取的定义


import configparser
import os
import time
import logging

#写日志的模块，格式，日志的位置 加 日志内容
def log(logfile,content):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        # 日期格式
    fp = logging.FileHandler(logfile, encoding='utf-8')
    fs = logging.StreamHandler()
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用
    logging.basicConfig(level=logging.DEBUG,handlers=[fp, fs])

    #logging.debug("This is a debug log.哈哈")
    logging.info(content)


def external_email():
#外部邮件的发送方法，可选方法，可配可不配
    import smtplib
    from email.header import Header
    from email.mime.text import MIMEText
    mail_host = "smtp.163.com"      # SMTP服务器
    mail_user = "18970078166"                  # 用户名
    mail_pass = "wjb711"               # 授权密码，非登录密码

    sender = '18970078166@163.com'    # 发件人邮箱(最好写全, 不然会失败)
    receivers = ['18970078166@163.com','10054053@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    title = '功能性测试'
    #global content
    #print ('content is:',content,type(content))
    content="this is for test"
    message = MIMEText(content, 'plain',"utf-8")  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

#读取配置文件，也就是上次一日志文件有多少行，如果没有就建一个新的配置文件，主要做第二次和第一次的差异比对
def config_read(file,section,name):
    configfile=file

    config=configparser.ConfigParser()
    config.read(configfile)
    try:

        value=config.get(section,name)
    #config.set(section, name, 'hello')
    #print (value)
        return value
    except:
        config='''
        [section1]
        len = 0
            '''
        with open(file,"w+") as f:
            f.write(config)
        return str(0)
#把当前日志行数写入配置文件中，方便下次比对
def config_write(file,section,name,value):
    configfile=file

    config=configparser.ConfigParser()
    config.read(configfile)

    config.set(section, name, value)

    with open(configfile,"w+") as f:
        config.write(f)

#主要做的处理
def action():
    #打开日志文件，这里选取的是ssh,sft之类的日志文件位置，可根据实际需要调整
    with open ('/var/log/secure','r') as file:
        lines=file.readlines()
        #first_line = lines[0] #取第一行
        #last_line = lines[-1]
    len0=len(lines)

    x=config_read('1.txt','section1','len')
#跟前一次日志行数作比对
    #如果有变化，日志增大
    if len0>int(x):
        print('something changed')
        #action()
        config_write('1.txt','section1','len',str(len0))
        mail=[]
        for i in range(int(x),len0):
            #判断日志中是否存在“failure”关键词
            if 'failure' in lines[i]:
                #print(lines[i])
                mail.append(lines[i]+'\n')
        #print(mail)
        if mail==[]:
            pass
        else:
            #print(mail)

            #x0,y0=re.search('rhost',mail[0]).span()
            #x1,y1=re.search('user=',mail[0]).span()
            print(mail[0])
            #从指定的字符串中抓取Ip信息，可以自定义
            ip=mail[0].split(' ')[13].replace('\n\n','').replace('rhost=','')
            log('/var/log/monitor_ip.log',ip)
            print(ip)
            #抓到IP后通过iptables锁定， sleep 半小时后解锁
            os.system('iptables -I INPUT -s '+ip+'/32 -j DROP&&sleep 1800&&iptables -D INPUT -s '+ip+'/32 -j DROP&')
            #如果需要出发邮件通知可以打开下面的注释
            #external_email()
    elif len0==int(x):
        print('no change')
    else:
        print('smaller,strange, change to 0 a new file')
        config_write('1.txt','section1','len',str(0))





if __name__=="__main__":
    print('start')
    #循坏每6秒执行一次
    while True:
        print('start0')

        action()
        time.sleep(6)
        print('hello......')
