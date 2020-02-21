
import configparser
import smtplib
from email.mime.text import MIMEText
import sys
CONFIGFILE=sys.argv[1]
print(CONFIGFILE)



def internal_email():
    #CONFIGFILE="config.txt"
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
#内部邮件的发送方法
    
    #from email.mime.multipart import MIMEMultipart
    
    #print ('hello')

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

