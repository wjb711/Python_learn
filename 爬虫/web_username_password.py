import pyautogui as p

#模拟键盘模块

import subprocess

#子进程模块，用来启动浏览器等其他操作

import time

#时间模块，用来输入时暂停时间

import datetime

#日期模块，用于写日志

from urllib.request import urlopen

#简单的网页加载模块，用来测试网页是否畅通

import easygui as g

#用来弹出警告信息

import os

#导入系统os模块

 

def upgrade(web):

#自定义升级模块，参数是ip.txt中的web链接

    prs=subprocess.Popen(["C:\\Program Files\\Internet Explorer\\iexplore.exe",  web])

    #打开IE浏览器，并打开指定web地址

    time.sleep(15)

    #等待n秒开始

    p.press('shift')

    #按下shift,防止搜狗输入法的默认中文设置，切成英文，如果终端机有其他输入法，可能要更改

    time.sleep(1)

    f=open('config.ini','r')

    #打开配置文件config.ini

    username=f.readlines()[1].replace('\n','')

admin    f=open('config.ini','r')

    #打开配置文件config.ini

    password=f.readlines()[2].replace('\n','')

    print (username)

    p.typewrite(username)

    time.sleep(1)

    p.press('tab')

    time.sleep(1)

    p.typewrite(password)

    time.sleep(1)

    p.typewrite('\n')admin

    time.sleep(1)

    p.typewrite(username)

    time.sleep(1)

    p.press('tab')

    time.sleep(1)

    p.typewrite(password)

    time.sleep(1)

    p.typewrite('\n')

    time.sleep(1)

    #以上为输入用户名和密码，这个网页需要输入两次

    f=open('config.ini','r')

    tab1=int(f.readlines()[3].replace('\n',''))

    print ('tab1 is ',tab1)

    #读取config.ini中的第4行作为tab按键数，注意在这里显示为3，因为python从0开始

    for i in range(tab1):

        p.press('tab')

        time.sleep(1)

 

 

    p.typewrite(' ')

    time.sleep(1)

    #按空格键选择文件

    print ('End0')

    f=open('config.ini','r')

    file=f.readlines()[4].replace('\n','')

    #选择config.ini中第五行作为上传文件

    time.sleep(1)

    p.typewrite(file)

    time.sleep(1)

    p.typewrite('\n')

    time.sleep(1)

    f=open('config.ini','r')

    tab2=int(f.readlines()[5].replace('\n',''))

    print ('tab2 is ',tab2)

    #读取config.ini中的第6行作为tab按键数，注意在这里显示为3，因为python从0开始

    for i in range(tab2):

        p.press('tab')

        time.sleep(1)

 

    p.typewrite('\n')

    time.sleep(1)

    time.sleep(15)

    #等待15秒上传文件时间

    print ('End2')

    p.keyDown('altleft')

    p.press('f4')

    p.keyUp('altleft')

    time.sleep(1)

    #以上是alt+F4关闭IE的做法

    print ('End1')

    time.sleep(1)

if __name__=='__main__':

#主函数，防止外部调用

   

    g.msgbox('Please close all IE')

    try:

        f=open('ip.txt','r')

        #检查是否有ip.txt文件，否则报错退出

        open('config.ini','r')

        #检查是否有config.ini文件，否则报错退出

    except:

        g.msgbox('no ip.txt or config.ini')

        #提示错误信息

        exit()

        #退出程序

    try:

        open('log.log','r').close()

        log=open('log.log','a')

        #查看是否有日志文件log.log

    except:

        open('log.log','w').close()

        log=open('log.log','a')

        #如果没有，则新建一个log.log日志文件

    for line in f.readlines():

        print (line)

        try:

            resp=urlopen(line,timeout=5)

            code=resp.getcode()

            print (code)

            #试着打开网站，如果超过5秒，则报错，写入日志，执行下一个

            upgrade(line)

           

            log.write('Success '+str(datetime.datetime.now())+line)

            #日志

        except:

            print (line,'line is not response')

            log.write('Failed '+str(datetime.datetime.now())+line)

            #日志报错写入

    log.close()

    #关闭日志写入功能

    g.msgbox('End')
