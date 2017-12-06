'''

本文是利用类似按键精灵的python模块pyautogui， 实现自动答题的目的

基本原理是建立题库， 把所有正确答案的图片都存下来， 当遇到问问题时，自动在页面上点击匹配到的正确图片

'''

import pyautogui as p

import time

import datetime

 

#日志功能， 记录哪个用户成功， 哪个用户失败

def log(user):

    try:

 

        open('log.log','r').close()

 

        log=open('log.log','a')

 

        #查看是否有日志文件log.log

 

    except:

 

        open('log.log','w').close()

 

        log=open('log.log','a')

    log.write('Success '+str(datetime.datetime.now())+user+'\n')

 

   

#从txt文档中提取用户名和密码

def username():

    i=0

    dict1={}

    try:

        while i<100:

            f=open('username.txt','r')

            username=f.readlines()[i].replace('\n','')

            f=open('username.txt','r')

            password=f.readlines()[i+1].replace('\n','')

            dict1[username]=password

            print ('y',i)

            i=i+2

    except:

        pass

    return dict1

 

 

#遇得输入文字的地方， 判断如果是搜狗中文开启， 则按shift切换为英文

def sogou_zhong():

    location_sogou_zhong=p.locateOnScreen('img\sogou_zhong.png')

    if location_sogou_zhong:

        p.typewrite(['shift'])

        time.sleep(2)

 

#这是一个核心模块， 找到给定的图片， 在屏幕上找到对应位置， 并点击

#        也就是答题模块

def click_pic(pic):

    location=p.locateCenterOnScreen('img//'+pic+'.png')

    print ('img//'+pic+'.png',location)

    if location:

       

        time.sleep(1)

        p.moveTo(location)

        time.sleep(1)

        p.click()

        time.sleep(1)

 

#这个和上一个类似， 找到给定的图片， 在屏幕上找到对应位置， 并拖拽平移

def drag_pic(pic):

    location=p.locateCenterOnScreen('img//'+pic+'.png')

    print ('img//'+pic+'.png',location)

    if location:

       

        time.sleep(1)

        p.moveTo(location)

        time.sleep(1)

        p.dragRel(0,-200,2)

        time.sleep(1)

 

#IE窗口最大化的功能快捷键      

def window_max():

    p.hotkey('alt','v')

    time.sleep(1)

    p.typewrite('f')

    time.sleep(1)

 

#遇到德文，切换为英文

def german():

    location_german=p.locateOnScreen('img\german.png')

    if location_german:

        print ('german')

        time.sleep(1)

        p.moveTo(p.center(location_german))

       

        time.sleep(1)

        location_english=p.locateOnScreen('img\english.png')

        p.moveTo(p.center(location_english))

        time.sleep(1)

        p.click()

        time.sleep(1)

       

#打开IE， 注意这里用到的是按着shift键， 邮件选择其他用户登录

def openie():

    p.moveTo(0,1,duration=1)

    p.typewrite(['win'])

    time.sleep(2)

    sogou_zhong()

    time.sleep(1)

    p.typewrite('iexplore.exe')

    time.sleep(1)

    #p.screenshot('foo.png')

 

    location_ie1=p.locateOnScreen('img\ie1.png')

    location_ie0=p.locateOnScreen('img\ie0.png')

    if location_ie0:

        print ('pass')

        #button7x, button7y = p.center(location_ie1)

        print (p.center(location_ie0))

        p.moveTo(p.center(location_ie0))

        #p.click()

        p.keyDown('shift')

        time.sleep(1)

        p.click(button='right')

        p.keyUp('shift')

        p.typewrite('f')

        time.sleep(1)

        p.typewrite(['shift'])

        time.sleep(3)

 

#主函数

if __name__=='__main__':

    #读取用户名密码

    dict1=username()

   

    print (dict1)

    #根据用户名密码每人执行一边程序

    for username,password in dict1.items():

        print ('username is',username)

        print ('password is',password)

        #打开IE

        openie()

        #切换中英文

        sogou_zhong()

        #输入用户名密码

        p.typewrite(username)

        p.typewrite(['tab'])

        p.typewrite(password)

        p.typewrite(['enter'])

        time.sleep(5)

        #p.typewrite(['F11'])

        #p.keyDown('ctrl')

        #time.sleep(1)

        #p.click(button='right')

        time.sleep(2)

        p.hotkey('ctrl','o')

        sogou_zhong()

        #输入网址

        p.typewrite('http://xxx.abc.com/')

        time.sleep(2)

        p.typewrite(['enter'])

        time.sleep(5)

        sogou_zhong()

        p.typewrite(username)

        p.typewrite(['tab'])

        p.typewrite(password)

        p.typewrite(['enter'])

        time.sleep(5)

        window_max()

        time.sleep(15)

        #p.hotkey('alt','f4')

        if p.locateCenterOnScreen('img/company.png'):

            print ('password correct for ',username)

            german()

            time.sleep(15)

            p.moveTo(p.locateCenterOnScreen('img/course.png'))

            p.moveRel(1100,None)

            p.click()

            time.sleep(1)

            p.click()

            time.sleep(30)

            click_pic('no')

            time.sleep(10)

        #p.alert('hello')

        #if p.locateCenterOnScreen('img/company.png'):

            #pass

            click_pic('back')

            time.sleep(3)

            click_pic('back1')

            time.sleep(10)

            i=0

            #下面是试题库， 每打开一页，都找正确答案匹配。

            while i<28:

                click_pic('q1')

                click_pic('q2')

                click_pic('q3a')

                click_pic('q3b')

                drag_pic('q4a')

                drag_pic('q4b')

                drag_pic('q4c')

                click_pic('q5')

                click_pic('q6a')

                click_pic('q6b')

                click_pic('q6c')

                click_pic('q7')

                click_pic('q8a')

                click_pic('q8b')

                click_pic('q8c')

                click_pic('q9a')

                click_pic('q9b')

                click_pic('q10')

                click_pic('q11a')

                click_pic('q11b')

                click_pic('q13a')

                click_pic('q13b')

                click_pic('ok')

                click_pic('next')

                p.moveRel(-100,None)

                time.sleep(10)

                i=i+1

            #题目完成后截图

            p.screenshot(username+'.png')

            p.hotkey('alt','f4')

            p.typewrite(['enter'])

            time.sleep(1)

            #记录日志

            log(username+'success')

        else:

            log(username+'failed')
