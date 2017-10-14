#我们公司的outlook由于安全原因做了限制自动转发的功能，
#所以我这里拼凑了一个脚本，模拟人工操作，时间自动转发
import win32com.client as win32

import win32com,os,time,_thread,datetime

shell = win32com.client.Dispatch("WScript.Shell")

def sendmail():

    print ('hello1')

    outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")

    print ('hello2')

    outbox = outlook.GetDefaultFolder(6)

    print ('hello3')

#try the restrict method!

    #messages = outbox.Items.restrict("[SentOn] > now - duration")

    print ("[SentOn] > '"+now1+"'")

    #messages = outbox.Items.restrict('"'"[SentOn] > "+now1+'"')

    #messages = outbox.Items.restrict("[SentOn] > '7/17/2017 17:53'")

    messages = outbox.Items.restrict("[SentOn] > '"+now1+"'")

    print ('hello4')

    for message in messages:

        print ('hello5')

        NewMsg = message.Forward()

        print ('hello6')

        _thread.start_new_thread(button0,(1,2))

        NewMsg.Body = message.Body

        print ('hello7')

        NewMsg.Subject = message.Subject

        print ('hello8')

        NewMsg.To = email

        print ('hello9')

        _thread.start_new_thread(button1,(1,2))

        NewMsg.Send()

 

 

def unsleep(a1,a2):
#防止电脑自动休眠或锁屏
   

    while 1>0:

       

 

        shell.SendKeys('%p')

        time.sleep(200)

def button0(a1,a2):
#按键

    time.sleep(3)

    shell.SendKeys('{TAB}')

    shell.SendKeys('{TAB}')

    shell.SendKeys('{TAB}')

    shell.SendKeys('{ENTER}')

    print ('hello0')

def button1(a1,a2):
#按键
   

    time.sleep(8)

    shell.SendKeys('{TAB}')

    shell.SendKeys('{TAB}')

    #shell.SendKeys('{TAB}')

    shell.SendKeys('{ENTER}')

    print ('hello0')

if __name__=='__main__':

    #duration=0:05:00

    email=input('your email address?')

    _thread.start_new_thread(unsleep,(1,2))

    now= datetime.datetime.now()
#日期时间及算法
    while 1>0:

       

        duration=datetime.datetime.now()-now

        now= datetime.datetime.now()

        now0=now.strftime("%m/%d/%Y %H:%M")

        now1=(now-duration).strftime("%m/%d/%Y %H:%M")

        print ('now is ',now0)

        print ('duration is ',duration)

        print ('now1 is ',now1)

        sendmail()

        time.sleep(20)
