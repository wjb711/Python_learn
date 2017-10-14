# -*- coding: cp936 -*-
import cv2
import numpy as np
import time
import sys
import datetime


cap=cv2.VideoCapture(0)


while(True):
    ret,img=cap.read()
    gray=cv2.cvtColor(img,6)
    ret,thresh=cv2.threshold(gray,60,255,cv2.THRESH_BINARY)
    eigen = cv2.cornerEigenValsAndVecs(thresh, 40, 3)
    flow = eigen[:,:,3]
    print eigen


    
    


    #cv2.imshow('img',img)
    #cv2.imshow('gray',gray)
    #cv2.imshow('thresh',thresh)
    #cv2.imshow('eigen',flow)
    cn=cv2.waitKey(0)
    
