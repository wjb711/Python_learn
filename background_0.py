import numpy as np
import cv2
import operator
from pandas import Series,DataFrame
import pandas as pd

cap = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))


fgbg =cv2.createBackgroundSubtractorKNN(history = 1, dist2Threshold=30,detectShadows=1)

while cv2.waitKey(1)!=27:
    ret, frame = cap.read()
    #gray=cv2.cvtColor(frame,6)
    
    blur = cv2.GaussianBlur(frame,(5,5),0)
    canny=cv2.Canny(blur,50,100)
    cv2.imshow('canny',canny)
    fgmask = fgbg.apply(canny)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    blur1 = cv2.GaussianBlur(fgmask,(5,5),0)
    cv2.imshow('blur1',blur1)
    ret,thresh=cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
    cv2.imshow('frame1',thresh)
    image, cnts, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    #cnts = max(cnts, key=cv2.contourArea)
    #cnts.index( max(cnts, key=cv2.contourArea) )
    #max_index, max_value = max(cnts, key=cv2.contourArea)
    #print max_index
    #cv2.drawContours(frame, cnts, 0, (0,255,255), 5)
    #print 'max is ',max(cnts, key=cv2.contourArea)
    #cv2.imshow('frame0',frame)

    #print 'max is ',max(cv2.contourArea(contours))
    #print max(cv2.contourArea(c) for c in cnts)
    #if cnts:
    #    print cnts 
    f1=frame.copy()
    #len0=len(contours)
    #print len0
    #i=0
    #max=2000
    #print 'len of cnts is ',len(cnts) 
    max=2000
    #i=0
    bg=np.zeros((480,640,3), np.int8)
    for i in range(len(cnts)):
        if cv2.contourArea(cnts[i]) > max:
            max = cv2.contourArea(cnts[i])
            maxIndex = i
            bg=cv2.drawContours(bg, cnts, i, (255,255,255), -1)
            #x,y,w,h = cv2.boundingRect(cnts[i])
            #centerX=(x+w)/2
            #centerY=(y+h)/2
            #print 'x is ',x,' y is ',y,' w is ',w,' h is ',h 
            #f2=frame[y:480,x:640]
            #frame[0:h*2,0:w*2]=frame[y:y+h,x:x+w]
            #cv2.imshow('hello',f2)
            #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #print 'max is ',max,'i is ',i

    cv2.imshow('frame0',frame)
    cv2.imshow('bg',bg)
    #cv2.imshow('blur',f2)
    #    cnt = contours[i]
    #    if cv2.contourArea(cnt) >2000:
            
    #        if cv2.contourArea(cnt) >max
    #            max=cv2.contourArea(cnt)
    #        cv2.drawContours(f1, contours, i, (0,255,255), 5)
        #print cnt(i)
    #    i=i+1
    #for cnt in contours:
    #    if cv2.contourArea(cnt) >2000:
    #        cv2.drawContours(f1, cnt, 5, (0,255,255), 5)
    #cv2.imshow('frame0',f1)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    #cv2.imshow('frame2',fgmask)
    #bitwise=cv2.bitwise_and(frame,frame,mask=fgmask)
    #cv2.imshow('bitwise',bitwise)

cap.release()
cv2.destroyAllWindows()
