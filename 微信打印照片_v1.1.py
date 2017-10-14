# -*- coding: cp936 -*-   #中文注释语句
#此程序的目的是创建一个webservice网页，网页上可以上传文件， 例如上传照片
#与此同时， 在文件夹内， 搜索对应后缀的文件，例如jpg, 搜到之后发送到打印机打印， 最后删除照片。
#也就是说手机访问此网页上传照片， 电脑从后台打印照片
#也就是类似微信打印机的功能。同理此脚本也可以改造为微信打印word, excel,pdf的程序， 稍加改造即可。
#如有问题，可以联系本人10054053@qq.com
#也可以在github上留言


#注意，本脚本的环境是python2.7，不适用python3， 成功后默认的地址是http://127.0.0.1:8000，对了是windows,具体我的是在win7上跑的。

#需要安装pywin32, 下载位置 https://sourceforge.net/projects/pywin32/





import os
import posixpath
import BaseHTTPServer
import urllib
import cgi
import shutil
import mimetypes
import re
import thread
import os,time,win32print,sys,win32ui
import cv2
import numpy as np
if sys.version_info >= (3,):
    print ('Error, you should run it in python 2.7, not 3.0+')
    input("press any key to continue")

#加载各类模块，本脚本大体分两个模块， 一个是http上传， 一个是搜索上传文件并打印。 

class Printer_:
    def printer(self,img):
        print ('C:/temp/i_view32.exe '+img+' /print')
        os.system('C:/temp/i_view32.exe '+img+' /print')
        print ('end')
    def yicun(self,end):
        for i in os.listdir('C:/Printer/net/WWW/1cun/php/files/'):
            print (i)
            if i.endswith(end) or i.endswith('.JPG'):
                all = np.ones((800, 1350,3), np.uint8)*255
                image=cv2.imread('C:/Printer/net/WWW/1cun/php/files/'+i)
                res=cv2.resize(image,(200,250),interpolation=cv2.INTER_CUBIC)
                all[50:300,100:300]=res
                all[50:300,300:500]=res
                all[50:300,500:700]=res
                all[50:300,700:900]=res
                all[50:300,900:1100]=res
                all[50:300,1100:1300]=res
                all[350:600,100:300]=res
                all[350:600,300:500]=res
                all[350:600,500:700]=res
                all[350:600,700:900]=res
                all[350:600,900:1100]=res
                all[350:600,1100:1300]=res

                #cv2.imshow('iker',res)
                #cv2.imshow('image',image)
                #cv2.imshow('image1',all)
                cv2.imwrite('1cun.jpg',all)
                #cv2.waitKey(0)
                #cv2.destoryAllWindows()
                os.remove('C:/Printer/net/WWW/1cun/php/files/'+i)
    
    def img(self,end):
        print ('start img')
        for i in os.listdir('./'):
            if i.endswith(end) or i.endswith('.JPG'):
                print (i)
                #os.system('print')
                print (i)
                self.printer(i)
                time.sleep(30)
                os.remove(i)
    def __init__(self): #初始化，并定义搜索后缀，这里默认是jpg
        print ('this is in Printer_')
        while 1>0:
            time.sleep(5)
            self.yicun('.jpg')
            self.img('.jpg')

def test(a1,a2):
    print ('ok')
    Printer_()
##这句很重要， 是建立一个并发程序， 当跑下面的http上传webservice的同时， 并发跑这个打印的模块
if __name__ == '__main__':
    print ('start')
    Printer_()
    
    #thread.start_new_thread(test,(1,2))
    time.sleep(3) 
