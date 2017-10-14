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
im1=cv2.imread('ren.jpg')
#前景图片
gray1=cv2.cvtColor(im1,6)
#灰度处理
ret,thresh1=cv2.threshold(gray1,127,255,cv2.THRESH_BINARY)
#阀值化
thresh1a=cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)
#转化通道
thresh1_INV=cv2.bitwise_not(thresh1)
#阀值取反
thresh1_INVa=cv2.cvtColor(thresh1_INV,cv2.COLOR_GRAY2BGR)
#转化通道
im2=cv2.imread('lufugong.jpg')
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
cv2.imshow('im_all',im_all)
cv2.waitKey(0)

