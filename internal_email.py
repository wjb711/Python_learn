import smtplib

def internal_email():


    from email.mime.text import MIMEText

    smtp = smtplib.SMTP()

    smtp.connect(mailserver_ip)

    msg = MIMEText(content, 'plain', 'utf-8')

    msg['Subject'] = title

    smtp.sendmail(sender, receivers, msg.as_string())

    smtp.quit()
mailserver_ip='10.4.172.3'
title='标题'
sender='jianbo.wang@gi-de.com'
receivers=['jianbo.wang@gi-de.com','10054053@qq.com']
content='邮件内容'
internal_email()
