import cv2
import numpy as np
from matplotlib import pyplot as plt
cap0=cv2.VideoCapture(0)
cap1=cv2.VideoCapture(1)
while cv2.waitKey(1)!=27:
    t0=cap0.grab()
    #print t0
    ret0, frame0=cap0.read()
    left=cv2.cvtColor(frame0,6)
    r1=cap0.retrieve()
    
    t1=cap1.grab()
    #cv2.imshow('0',t1)
    r2=cap1.retrieve()
    ret1, frame1=cap1.read()
    right=cv2.cvtColor(frame1,6)
    stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET,ndisparities=16, SADWindowSize=15)
    disparity = stereo.compute(left,right)
    #print t1
    #print frame0
    
    #ret1, frame1=cap1.read()
    #print frame1
    cv2.imshow('0',frame0)
    #ret1, frame1=cap1.read()
    cv2.imshow('1',frame1)

    #cv2.imshow('2',disparity)
    #plt.imshow(disparity,'gray')
    #plt.show()
    #cv2.waitKey(50)
cap0.release()
cap1.release()
cv2.destroyAllWindows()
    
    
    
