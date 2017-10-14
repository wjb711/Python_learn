# -*- coding: cp936 -*-
import cv2
import sys
import numpy as np
def nothing(x):
    pass
fn = sys.argv[1]
im1=cv2.imread(fn)
cv2.namedWindow('颜色捕捉',0)
cv2.createTrackbar('阀值最低', '颜色捕捉', 255, 255, nothing)
cv2.createTrackbar('阀值最高', '颜色捕捉', 255, 255, nothing)
while(1):
    gray=cv2.cvtColor(im1,6)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thrs1 = cv2.getTrackbarPos('阀值最低', '颜色捕捉')
    thrs2 = cv2.getTrackbarPos('阀值最高', '颜色捕捉')
    edged = cv2.Canny(gray, thrs1, thrs2)
    cv2.imshow('1',im1)
    image, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #image, cnts, hierarchy = cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cnt=cnts[1]
    for cnt in cnts:
        if cv2.contourArea(cnt) > 10000:
            
        
    #leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
            leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
            rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
            topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
            bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
            img = cv2.circle(im1,leftmost, 0, (0,0,255), -1)
            img = cv2.circle(im1,rightmost, 0, (0,0,255), -1)
            img = cv2.circle(im1,topmost, 0, (0,0,255), -1)
            img = cv2.circle(im1,bottommost, 0, (0,0,255), -1)
    #print  leftmost
    #break

    rect = np.zeros((4, 2), dtype = "float32")
    rect[0]=leftmost
    rect[1]=topmost
    rect[2]=rightmost
    rect[3]=bottommost
    maxWidth=200
    maxHeight=300
    dst = np.array([[0, 0],[maxWidth - 1, 0],[maxWidth - 1, maxHeight - 1],[0, maxHeight - 1]], dtype = "float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(im1, M, (maxWidth, maxHeight))
    cv2.imshow("Outline", im1)
    cv2.imshow("M", M)
    cv2.imshow('gray',gray)
    cv2.imshow('blur',blur)
    cv2.imshow('颜色捕捉',edged)
    cv2.imshow('warped',warped)
    cv2.waitKey(30)
    #break
