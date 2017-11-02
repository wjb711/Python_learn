import win32com.client as win32

 

import win32com,os,time,_thread,datetime

import easygui as g

from win32gui import *

 

import win32gui

#导入各类模块

 

shell = win32com.client.Dispatch("WScript.Shell")

 

#运行环境

 

def sendmail():

    #发送邮件

 

   

 

    outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")

    #调用outlook的接口

   

 

    outbox = outlook.GetDefaultFolder(6)

 

 

 

    messages = outbox.Items.restrict("[SentOn] > '"+sftime+"'")

    #按选定的时间发送

   

 

   

 

    for message in messages:

    #如果有多个邮件，循环发送

 

       

 

        NewMsg = message.Forward()

 

        #print ('hello6')

        title='Microsoft Outlook'

        w1hd=FindWindow(0,title)

        #print ('h1hd is ',w1hd)

        #ShowWindow(w1hd,win32con.SW_SHOWNORMAL)

 

        win32gui.ShowWindow(w1hd, 3)

        win32gui.SetActiveWindow(w1hd)

        win32gui.BringWindowToTop(w1hd)

        win32gui.SetForegroundWindow(w1hd)

 

        #上面这一段是把邮件的窗口激活

 

        _thread.start_new_thread(button0,(1,2))

 

        NewMsg.Body = message.Body

 

        #print ('hello7')

 

        NewMsg.Subject = message.Subject

 

        #print ('hello8')

 

        NewMsg.To = email

 

        #print ('hello9')

 

        _thread.start_new_thread(button1,(1,2))

 

        NewMsg.Send()

        #上面是邮件的标题，内容， 目标用户等

 

def unsleep(a1,a2):

#防止电脑自动休眠或锁屏

  

 

    while 1>0:

 

      

 

 

 

        shell.SendKeys('%p')

 

        time.sleep(200)

 

def button0(a1,a2):

 

#按键

 

    time.sleep(1)

 

    shell.SendKeys('{TAB}')

 

    shell.SendKeys('{TAB}')

 

    shell.SendKeys('{TAB}')

 

    shell.SendKeys('{ENTER}')

 

    #print ('hello0')

 

def button1(a1,a2):

#按键

  

 

    time.sleep(6)

 

    shell.SendKeys('{TAB}')

 

    shell.SendKeys('{TAB}')

 

    #shell.SendKeys('{TAB}')

 

    shell.SendKeys('{ENTER}')

 

    #print ('hello0')

 

if __name__=='__main__':

 

    #duration=0:05:00

    email=g.enterbox('your private email address?',title='outlook小插件')

    g.msgbox('请最小化黑色DOS，勿关闭，勿锁屏')

    #email=input('your email address?')

 

    _thread.start_new_thread(unsleep,(1,2))

 

   

    now0=datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    #print (now[4:6])

    sched_Timer=datetime.datetime(int(now0[0:4]),int(now0[4:6]),int(now0[6:8]),int(now0[8:10]),int(now0[10:12])+1,0)

    #print (sched_Timer)

 

while True:

    now=datetime.datetime.now()

    if now>sched_Timer:

        #print ('y')

        sched_Timer=sched_Timer+datetime.timedelta(minutes=1)

        print (sched_Timer)

    else:

        #print ('n')

        pass

 

 

 

 

    while True:

        now=datetime.datetime.now()

        if now>sched_Timer:

        #print ('y')

            sftime=(sched_Timer-datetime.timedelta(minutes=1)).strftime("%m/%d/%Y %H:%M")

            #print ('sfttime is ',sftime)

            sched_Timer=sched_Timer+datetime.timedelta(minutes=1)

            #print (sched_Timer)

            try:

 

                sendmail()

            except:

                pass

           

        else:

       

            pass
