import cv2
import numpy as np
drawing = False
drawing1=False

def draw_circle(event,x,y,flags,param):
    global drawing,drawing1
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    if event == cv2.EVENT_RBUTTONDOWN:
        drawing1 = True
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
        if drawing1 == True:
            cv2.circle(img,(x,y),5,(0,255,0),-1)
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
    if event == cv2.EVENT_RBUTTONUP:
        drawing1 = False
    #print (drawing)

    
img=np.zeros((480,640,3),np.uint8)
cv2.namedWindow('img',0)
cv2.setMouseCallback('img',draw_circle)
while 1:
    cv2.imshow('img',img)
    cv2.waitKey(30)
cv2.destroyAllWindows()
