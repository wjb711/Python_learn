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
如提示如下错误:
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
import datetime
from common import Sketcher
from color_transfer import color_transfer
#import win32com
#import speech

#加载语音模块
def nothing(x):
    pass
def draw_circle(event,x,y,flags,param):
    #if event == cv2.EVENT_LBUTTONDBLCLK:
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('mouse x and y is ')
        print (x,y)
        px = im1[y,x]
        print ('RGB Value:')
        print px
        px_hsv = cv2.cvtColor(im1, cv2.COLOR_BGR2HSV)
        H=px_hsv.item(y,x,0)
        S=px_hsv.item(y,x,1)
        V=px_hsv.item(y,x,2)
        print ('HSV Value: H是颜色，S是纯度，V是亮度')
        print (H,S,V)


print(__doc__)
#显示前面绿色的声明的内容
print ('当前opencv版本为'+cv2.__version__)
#显示opencv版本
print ('你的python版本信息为')
print (sys.version_info)
#speech.say("推荐使用720p或1080p高清摄像头")

#cv2.namedWindow('mix',0)
#print sys.argv[0],sys.argv[1]

cap=cv2.VideoCapture(0)
ret = cap.set(3,960)
ret = cap.set(4,720)
try:
    fn = sys.argv[1]
    
    #尝试获得命令的第一个参数， 也就是图片的名字
except:
    fn = 'images/lufugong.jpg'
#fn = cv2.resize(fn,(640, 480), interpolation = cv2.INTER_CUBIC)
print ('第一个参数是')
#print   sys.argv[1]   
print fn
    #如果找不到上面指定的图片名称， 默认名称为lufugong.jpg
#尝试用1280x960打开摄像头， 如果失败， 使用默认的640x480

print ('start here')
print ('实际分辨率为')
y1=cap.get(3)
x1=cap.get(4)
print y1,x1
#ret = cap.set(3,1280)
#ret = cap.set(4,720)
c=1
d=0

#im = cv2.imread(fn)

#im_white= cv2.imread('images/white.jpg')
im = cv2.imread(fn)
if x1==480.0:
    print ('480')
    im = cv2.resize(im,(640, 480), interpolation = cv2.INTER_CUBIC)
else:
    im = cv2.resize(im,(960, 720), interpolation = cv2.INTER_CUBIC)
cv2.namedWindow('颜色捕捉')
cv2.namedWindow('123',0)

cv2.setMouseCallback('颜色捕捉',draw_circle)
cv2.createTrackbar('色彩最低', '颜色捕捉', 74, 255, nothing)
cv2.createTrackbar('色彩最高', '颜色捕捉', 122, 255, nothing)
cv2.createTrackbar('纯度最低', '颜色捕捉', 9, 255, nothing)
cv2.createTrackbar('纯度最高', '颜色捕捉', 56, 255, nothing)
cv2.createTrackbar('亮度最低', '颜色捕捉', 133, 255, nothing)
cv2.createTrackbar('亮度最高', '颜色捕捉', 255, 255, nothing)
cv2.createTrackbar('模糊度', '颜色捕捉', 4, 100, nothing)


while (True):

    ret,im1=cap.read()
        
    #cv2.imshow('原图',frame)
    #原图
    #gray = cv2.cvtColor(frame, 6)
    #cv2.imshow('原图灰度',gray)
    #灰度图
    # Convert BGR to HSV
    hsv = cv2.cvtColor(im1, cv2.COLOR_BGR2HSV)

    thrs1 = cv2.getTrackbarPos('色彩最低', '颜色捕捉')
    thrs2 = cv2.getTrackbarPos('色彩最高', '颜色捕捉')
    thrs3 = cv2.getTrackbarPos('纯度最低', '颜色捕捉')
    thrs4 = cv2.getTrackbarPos('纯度最高', '颜色捕捉')
    thrs5 = cv2.getTrackbarPos('亮度最低', '颜色捕捉')
    thrs6 = cv2.getTrackbarPos('亮度最高', '颜色捕捉')
    thrs7 = cv2.getTrackbarPos('模糊度', '颜色捕捉')
    thrs7=thrs7+1
    #print mode
    #print thrs1

#im1=cv2.imread('ren.jpg')
    #cv2.imshow('1',im1)
#前景图片
    #gray1=cv2.cvtColor(im1,6)
#灰度处理
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    thresh1 = cv2.inRange(hsv, lower_blue, upper_blue)
    blur = cv2.blur(thresh1,(thrs7,thrs7),0)
    ret3,thresh1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = np.ones((5,5),np.uint8)
    #thresh1 = cv2.erosion(thresh1,kernel,iterations = 1)

    #thresh1_INV=cv2.bitwise_not(mask)

    #ret,thresh1=cv2.threshold(gray1,thrs1,thrs2,cv2.THRESH_BINARY)
    #cv2.imshow('thresh1',thresh1)
#阀值化
    thresh1a=cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)
#转化通道
    thresh1_INV=cv2.bitwise_not(thresh1)
#阀值取反
    thresh1_INVa=cv2.cvtColor(thresh1_INV,cv2.COLOR_GRAY2BGR)
#转化通道
    im2=cv2.imread(fn)
    im2=im
#背景图

    im1_FG=color_transfer(im2,im1)
    #把背景图上色
    im_FG=cv2.add(im1_FG,thresh1a)
    #cv2.imshow('1',im_FG)
    #im_FG=color_transfer(im2,im_FG)
    #cv2.imshow('2',im_FG)
#前景图把人物抠出来

    im_BG=cv2.add(im2,thresh1_INVa)
#背景图把人物阴影去除
    im_all=cv2.bitwise_and(im_FG,im_BG)
    #center = (0, 0)
    #mixed_clone = cv2.seamlessClone(im_FG, im2, thresh1, center, cv2.MIXED_CLONE)
#合并人物和背景
#cv2.imshow('s1',im1)
#cv2.imshow('s2',im2)
#cv2.imshow('im3',im3)
#cv2.imshow('im_BG',im_BG)
#cv2.imshow('im_FG',im_FG)
    cv2.imshow('颜色捕捉',im_all)
    cv2.imshow('123',im_all)
    #cv2.imshow('456',mixed_clone)
    cn=cv2.waitKey(50)
    if cn==ord(' '):
        d=c+1
    if c==d:
        print ('0')
        cn=cv2.waitKey(30)
        now = datetime.datetime.now()
            #print ("yes")
        im_name1=(now.strftime('%Y-%m-%d_%H%M%S')+'.jpg')
        img_mark = im_all.copy()
        mark = np.zeros(im_all.shape[:2], np.uint8)
        sketch = Sketcher('可编辑', [img_mark, mark], lambda : ((255, 255, 255), 255))
        while(cn!=27):
            cn=cv2.waitKey(10)

            
            res = cv2.inpaint(img_mark, mark, 3, cv2.INPAINT_TELEA)
            cv2.imshow('可编辑',res)
            print cn
            print 'yes'
        #
        
        cv2.imwrite('images/'+im_name1,res)
        cv2.imshow('可编辑',res)
        cv2.waitKey(2000)
        cv2.destroyWindow('可编辑')
        print ('done')
    c=c+1
        

############################################################
    

