# -*- coding: cp936 -*-
import cv2
import numpy as np
import time
import sys
import datetime

cap=cv2.VideoCapture(0)
img1=cv2.imread('1.jpg')
while(True):
    ret,img2=cap.read()
    diff = cv2.absdiff(img1, img2)
    cv2.imshow('Photo',img2)
    cv2.imshow('diff',diff)
    cv2.waitKey(50)
        
        
