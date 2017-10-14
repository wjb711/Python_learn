import cv2

import numpy as np

def nothing(x):

    pass

cv2.namedWindow('image')

cv2.createTrackbar('a1','image',0,255,nothing)

cv2.createTrackbar('a2','image',255,255,nothing)

cv2.createTrackbar('a3','image',0,255,nothing)

cv2.createTrackbar('a4','image',255,255,nothing)

cv2.createTrackbar('a5','image',0,255,nothing)

cv2.createTrackbar('a6','image',255,255,nothing)

 

cap=cv2.VideoCapture(0)

while cv2.waitKey(10)!=27:

    a1 = cv2.getTrackbarPos('a1','image')

    a2 = cv2.getTrackbarPos('a2','image')

    a3 = cv2.getTrackbarPos('a3','image')

    a4 = cv2.getTrackbarPos('a4','image')

    a5 = cv2.getTrackbarPos('a5','image')

    a6 = cv2.getTrackbarPos('a6','image')

    _,frame=cap.read()

    blur=cv2.blur(frame,(10,10),0)

    lab=cv2.cvtColor(blur,cv2.COLOR_BGR2LAB)

    lower_blue = np.array([a1,a3,a5])

    upper_blue = np.array([a2,a4,a6])

 

    # Threshold the HSV image to get only blue colors

    mask = cv2.inRange(lab, lower_blue, upper_blue)

 

    # Bitwise-AND mask and original image

    #res = cv2.bitwise_and(lab,lab, mask= mask)

 

    #cv2.imshow('frame',frame)

    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('image',res)

    #cv2.imshow('res',res)

    #lab1=cv2.cvtColor(res,cv2.COLOR_LAB2BGR)

    #cv2.imshow('frame',lab1)

    

cap.release()

cv2.destroyAllWindows()
