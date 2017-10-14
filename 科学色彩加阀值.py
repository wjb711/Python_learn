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
cv2.createTrackbar('色彩选择', '视频色彩', 1, 250, nothing)
#cv2.createTrackbar('阀值', '视频色彩', 60, 255, nothing)

cap=cv2.VideoCapture(0)
while(1):
    ret,im=cap.read()
    #dst = cv2.detailEnhance(im, sigma_s=10, sigma_r=0.15)

    #gray=cv2.cvtColor(im,6)
    
    #im=cv2.imread('3.jpg')
    thrs1 = cv2.getTrackbarPos('色彩选择', '视频色彩')
    dst = cv2.detailEnhance(im, sigma_s=thrs1, sigma_r=0.2)
    #edges = cv2.Canny(dst, 50, 150, apertureSize = 3)  

    cv2.imshow("视频色彩", dst)
    cv2.imshow("edges", edges)
    cv2.imshow("im", im)
    cv2.imshow("result", result)
    cv2.waitKey(10);
