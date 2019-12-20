#本脚本的目的是对门禁系统的后台数据库sqlserver做查询， 找到进入的列表和出去的列表， 做差值， 就得出当前的在线人员名单和数量， 当达到某些条件是，语音报警


import pymssql
import datetime
import tkinter as tk
import time
import logging
import pyttsx3


#语音播报函数
def voice(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


#日志函数
def log(filename,info):
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info(info)


#差量函数， 用来读卡器的进入人员减去出去人员，得出结果当前数据室里的的人员名单的函数，使用了递归
def test(l0,l1):
    for x in l0:
        for y in l1:
            #print('x',x,'y',y)
            #a=input('a')
            if x==y:
                l0.remove(x)
                l1.remove(y)
                #print('l0:',l0)
                #print('l1:',l1)
                break
        #break
    #print('hello:',l0)
    if l1==[]:
        #print('END!!!')
        return l0
    else:
        return test(l0,l1)

    
#sql查询，主要查两个， 进入和出来的名单
def sqlserver():
    serverName = "localhost"
    #登陆用户名和密码
    userName = 'sa'
    passWord = '20184444.com'
    #today='2018-10-10'
    today = datetime.date.today()
    now=str(datetime.datetime.now())[:19]
    value='2018-10-10'
    #value=today

    #建立连接并获取cursor
    conn = pymssql.connect(serverName, userName , passWord, "door")
    cur = conn.cursor()
    #print("select logName from UserLog where logController=2 and logReader=3 and logEvent='0401' and logDate='"+date0+"'")
    #cur.execute("select logName from UserLog where logController=2 and logReader=3 and logEvent='0401' and logDate='2018-10-16'")
    #list_out=cur.execute("select logName from UserLog where logController=2 and logReader=4 and logEvent='0401' and logDate='2018-10-10'")
    cur.execute("select logName from UserLog where logController=2 and logReader=3 and logEvent='0401' and logName!='车间参观卡' and logDate=%s",value)

    list_in=cur.fetchall()
    print ('List_in:',list_in)
    cur.execute("select logName from UserLog where logController=2 and logReader=4 and logEvent='0401' and logName!='车间参观卡' and logDate=%s",value)
    list_out=cur.fetchall()
    print ('List_out:',list_out)
    cur.close()
    conn.close()
    lastone=test(list_in, list_out)
    print('当前：',str(lastone))
    return lastone
    #print(lastone,len(lastone))


#程序界面GUI函数
def monitor():
    window=tk.Tk()
    window.wm_attributes('-topmost', 1)

    window.title("数据室人数监控")
    position_x=window.winfo_screenwidth()-150
    window.geometry('%dx%d+%d+%d' % (750,80,(window.winfo_screenwidth()-750), (window.winfo_screenheight() -100) ))
    now=str(datetime.datetime.now())
            #num=1
            

    x=tk.Label(window, text='jello')
    x.config(text=now)
    x.pack()
    print('start')
    while True:
        #now=str(datetime.datetime.now())[:19]
        #q=Pool()
        list0=set(sqlserver())
        #q.close()
        #q.join()
        #print(list0.get())
        #list0=set(sqlserver())
        #now=str(list0)
        try:
            if len(list0)==1:
                log('log.txt',str(list0))
                x.config(text=str(list0),bg='red',font=15)
                voice(str(list0)+'单人进入数据室不合要求')
            else:
                x.config(text=str(list0),bg='green',font=8)
        except:
            pass
        #time.sleep(20)
        window.update()
        print('here1')
        #time.sleep(30)
        #window.after(60000)

#主函数运行
monitor()


    
