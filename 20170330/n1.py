# -*- coding: cp936 -*-
import cv2
import numpy as np
import time
import sys
import datetime

cap=cv2.VideoCapture(0)
while(True):
    ret,img=cap.read()

    cv2.imshow('简笔画',img)
    cn=cv2.waitKey(5)
    if cn==ord(" "):
        now = datetime.datetime.now()
            #print ("yes")
        im_name1=(now.strftime('%Y-%m-%d_%H%M%S')+'.jpg')
        
        cv2.imwrite('images/'+im_name1,img)
        cv2.imshow('Photo',img)
        cv2.waitKey(2000)
        cv2.destroyWindow('Photo')
        
