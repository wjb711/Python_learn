#此为邮件发送方法 通过命令和配置文件， 触发邮件发送

import configparser
import smtplib
from email.mime.text import MIMEText
import sys


#配置文件选取命令后第一个参数， 也就是config.ini
CONFIGFILE=sys.argv[1]
print(CONFIGFILE)


#定义内部邮件的函数
def internal_email():
    
    config=configparser.ConfigParser()
    config.read(CONFIGFILE)
    
    print(config['DEFAULT']['mail_server'])
    mail_server=config['DEFAULT']['mail_server']

    print(config['DEFAULT']['sender'])
    sender=config['DEFAULT']['sender']

    print(config['DEFAULT']['receivers'])
    receivers=config['DEFAULT']['receivers']

    print(config['DEFAULT']['title'])
    title=config['DEFAULT']['title']

    print(config['DEFAULT']['sender'])
    sender=config['DEFAULT']['sender']

    print(config['DEFAULT']['content'])
    content=config['DEFAULT']['content']


    smtp = smtplib.SMTP()
    
    
    smtp.connect(mail_server)


    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = title
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()

internal_email()
#另：config.ini文件样例如下
#[DEFAULT]
#mail_server = 10.x.172.x
#sender = tuzi@china.com
#receivers = renming@china.com
#title = title0
#content = content0

