import os,time,sys
def help():
    if len(sys.argv)==4:
        print ("您的设定为",sys.argv[1],sys.argv[2],sys.argv[3])
        pass
    else:
        
        print ("请按下面的格式放置参数 本程序.exe '文件件位置' 时间间隔(秒) 收件人邮箱地址")
        a=input('有问题可以联系xxx，按任意键退出')
        exit()
def email():
    import smtplib
    #from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    print ('时间差',time_delta,"小于设定值",time0,'所以触发邮件通知')

    smtp = smtplib.SMTP() 
    smtp.connect('your smtp server') 
    #smtp.login(username, password)
    #msg = MIMEMultipart('mixed')
    msg = MIMEText(str(os.listdir(foldername)), 'plain', 'utf-8')
    msg['Subject'] = foldername+'有更新'
    smtp.sendmail(email_address, email_address, msg.as_string()) 
    smtp.quit()
    print ('邮件发送完成',email_address,'请注意查收')

#
if __name__=='__main__':
    print ("欢迎使用本程序")
    print ("本程序的目的是为了实现当侦测到某文件夹内有新增或者文件变化时，触发邮件通知收件人")
    
    help()
    foldername=sys.argv[1]
    #print (foldername)
    #print (os.listdir(foldername))
    time0=sys.argv[2]
    email_address=sys.argv[3]
    #print (sys.argv[1])
    time_delta=int(time.time()-os.stat(foldername).st_mtime)
    print ("时间差为（秒）", time_delta)
    if time_delta<=int(time0):
        email()
    else:
        print ('超过了您的预设值',time0,'不会触发任何指令，退出')
        
    print ('结束')
