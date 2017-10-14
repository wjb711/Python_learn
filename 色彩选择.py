# -*- coding: cp936 -*-

'''
    OpenCV Colormap  Example
    
    Copyright 2015 by Satya Mallick <spmallick@learnopencv.com>
    
'''


import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow('视频色彩',0)
cv2.createTrackbar('色彩选择', '视频色彩', 0, 11, nothing)

cap=cv2.VideoCapture(0)
while(1):
    ret,im=cap.read()
    #im=cv2.imread('3.jpg')
    im = cv2.detailEnhance(im, sigma_s=10, sigma_r=0.15)
    thrs1 = cv2.getTrackbarPos('色彩选择', '视频色彩')
    print thrs1
    im_color0 = cv2.applyColorMap(im, thrs1)
    cv2.imshow("视频色彩", im_color0)
    cv2.imshow("im", im)
    cv2.waitKey(30);
