# -*- coding: cp936 -*-
import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(0)
#src=cv2.imread('1.png',-1)
cv2.namedWindow('a1',0)
#创建一个名字叫edge的新窗口，用来显示加工后的效果图， 0的意思是， 窗口可伸缩
cv2.createTrackbar('value', 'a1', 203, 254, nothing)
while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    #frame=src
    gray = cv2.cvtColor(frame, 6)

    # define range of blue color in HSV
    value = cv2.getTrackbarPos('value', 'a1')
    value=value+1
    i=value
    i1=value+10
    #print (i,i1)
    lower_blue = np.array([i])
    upper_blue = np.array([i1])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(gray, lower_blue, upper_blue)
    copy=frame.copy

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_not(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    cv2.imshow('a1',mask)
    #cv2.imshow('gray',gray)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
