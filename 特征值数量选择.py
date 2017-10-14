# -*- coding: cp936 -*-
import cv2

def nothing(x):
    pass
cap=cv2.VideoCapture(0)
ret = cap.set(3,960)
ret = cap.set(4,720)
cv2.namedWindow('简笔画',0)
cv2.createTrackbar('阀值', '简笔画', 203, 3000, nothing)
#cv2.createTrackbar('翻转', '简笔画', 500, 2000, nothing)
while(1):
    ret,img=cap.read()
    #im=cv2.imread('1.jpg')
    gray=cv2.cvtColor(img,6)
    thrs1 = cv2.getTrackbarPos('阀值', '简笔画')
    #thrs2 = cv2.getTrackbarPos('翻转', '简笔画')
    

    surf=cv2.SURF(thrs1)
    #detector = cv2.SIFT()
    #sift = cv2.SIFT()
    #surf.hessianThreshold = thrs2
    surf.upright = True
    kp, des = surf.detectAndCompute(gray,None)
    #keypoints = detector.detect(gray,None)  
    #img = cv2.drawKeypoints(img,keypoints)
    #img = cv2.drawKeypoints(img,kp)
    img=cv2.drawKeypoints(img,kp,None,(255,0,0),4)
    cv2.imshow('简笔画',img)
    cv2.imshow('gray',gray)
    print len(kp)
    cv2.waitKey(100)
