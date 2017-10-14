# -*- coding: cp936 -*-
#中文，你懂得
#!/usr/bin/python
'''
人在家中， 周游世界， 与世界各地风景名胜合影
用法如下
#用法python pan_painting.py  你的图片 例如 python pan_painting.py  time.jpg
#此脚本是windows环境python 2.7+opencv3.2版本的， 配置见下面的链接
https://github.com/wjb711/Opencv_learning/blob/master/windows_python2.7_opencv3.2%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E6%8C%87%E5%AF%BC.txt
#需要提前安装speech模块， 安装方法pip install speech
如提示如下错误
no module named win32com.client错误解决
请下载对应pywin32插件
https://sourceforge.net/projects/pywin32/files/pywin32/
到这里下载微软tts
http://www.microsoft.com/en-us/download/confirmation.aspx?id=27224
'''


import cv2
import numpy as np
import time
import sys
#import win32com
#import speech

#加载语音模块
def nothing(x):
    pass


print(__doc__)
#显示前面绿色的声明的内容
print ('当前opencv版本为'+cv2.__version__)
#显示opencv版本
print ('你的python版本信息为')
print (sys.version_info)
#speech.say("推荐使用720p或1080p高清摄像头")

cv2.namedWindow('mix',0)

cap=cv2.VideoCapture(0)
try:
        
    ret = cap.set(3,1280)
    ret = cap.set(3,960)
    y1=1280
    x1=960

except:
    ret = cap.set(3,640)
    ret = cap.set(3,480)
    y1=640
    x1=480
try:
    fn = sys.argv[1]
    #尝试获得命令的第一个参数， 也就是图片的名字
except:
    fn = 'images/lufugong.jpg'
    print fn
    #如果找不到上面指定的图片名称， 默认名称为lufugong.jpg
#尝试用1280x960打开摄像头， 如果失败， 使用默认的640x480
print ('实际分辨率为')
print cap.get(3)
print cap.get(4)
#ret = cap.set(3,1280)
#ret = cap.set(4,720)
c=1
d=0
im = cv2.imread(fn)

im_white= cv2.imread('images/white.jpg')
im = cv2.imread(fn)
cv2.namedWindow('颜色捕捉',0)
cv2.createTrackbar('阀值最低', '颜色捕捉', 0, 255, nothing)
cv2.createTrackbar('阀值最高', '颜色捕捉', 255, 255, nothing)
#cv2.createTrackbar('纯度最低', '颜色捕捉', 0, 255, nothing)
#cv2.createTrackbar('纯度最高', '颜色捕捉', 255, 255, nothing)
#cv2.createTrackbar('亮度最低', '颜色捕捉', 0, 255, nothing)
#cv2.createTrackbar('亮度最高', '颜色捕捉', 255, 255, nothing)

while (True):

    ret,im1=cap.read()
        
    #cv2.imshow('原图',frame)
    #原图
    #gray = cv2.cvtColor(frame, 6)
    #cv2.imshow('原图灰度',gray)
    #灰度图
    # Convert BGR to HSV
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thrs1 = cv2.getTrackbarPos('阀值最低', '颜色捕捉')
    thrs2 = cv2.getTrackbarPos('阀值最高', '颜色捕捉')
    #thrs3 = cv2.getTrackbarPos('纯度最低', '颜色捕捉')
    #thrs4 = cv2.getTrackbarPos('纯度最高', '颜色捕捉')
    #thrs5 = cv2.getTrackbarPos('亮度最低', '颜色捕捉')
    #thrs6 = cv2.getTrackbarPos('亮度最高', '颜色捕捉')

#im1=cv2.imread('ren.jpg')
    cv2.imshow('1',im1)
#前景图片
    b,g,r = cv2.split(im1)
    #gray1=cv2.cvtColor(im1,6)
#灰度处理
    ret,thresh1=cv2.threshold(g,thrs1,thrs2,cv2.THRESH_BINARY)
    cv2.imshow('thresh1',thresh1)
#阀值化
    thresh1a=cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)
#转化通道
    thresh1_INV=cv2.bitwise_not(thresh1)
#阀值取反
    thresh1_INVa=cv2.cvtColor(thresh1_INV,cv2.COLOR_GRAY2BGR)
#转化通道
    im2=cv2.imread(fn)
#背景图


    im_FG=cv2.add(im1,thresh1a)
#前景图把人物抠出来

    im_BG=cv2.add(im2,thresh1_INVa)
#背景图把人物阴影去除
    im_all=cv2.bitwise_and(im_FG,im_BG)
#合并人物和背景
#cv2.imshow('s1',im1)
#cv2.imshow('s2',im2)
#cv2.imshow('im3',im3)
#cv2.imshow('im_BG',im_BG)
#cv2.imshow('im_FG',im_FG)
    cv2.imshow('颜色捕捉',im_all)
    cv2.waitKey(50)

############################################################
    

