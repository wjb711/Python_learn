import cv2
import numpy as np
def give_X_Y(event,x,y,flags, param):
    print '1'
    if event==cv2.EVENT_MOUSEMOVE:
        print x,y
    
img1=np.zeros((480,640,3),np.uint8)
cv2.namedWindow('img',0)
cv2.setMouseCallback('img',give_X_Y)

print img1.shape

while(1):

    cv2.imshow('img',img1)
    #print '2'
    cv2.waitKey(30)
