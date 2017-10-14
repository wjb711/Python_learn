# -*- coding: cp936 -*-
import cv2
import numpy as np
import time
import sys
import datetime
def nothing(x):
    pass

cap=cv2.VideoCapture(0)
im1=cv2.imread('1.jpg')
im2=cv2.imread('2.jpg')
#cv2.namedWindow('mix',0)
cv2.namedWindow('颜色捕捉',0)
cv2.namedWindow('2',0)

while(True):
    ret,img=cap.read()


    
    cn=cv2.waitKey(5)
    if cn==ord("1"):
        im1=img
    if cn==ord("2"):
        im2=img
    diff = cv2.absdiff(im1, img)
    im_FG=cv2.add(im1,diff)
    #blur = cv2.GaussianBlur(diff,(5,5),0)

    cv2.imshow('2',im_FG)
    cv2.imshow('diff',diff)
    
