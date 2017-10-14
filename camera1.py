import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
cap.set(4,720)
#cap.set(15, 2.0)
#cap.set(5,30)
#cap.set(15,1)
#cap.set(14,250)
#cap.set(12,250)
#cap.set(13,10)
#cap.set(10,250)#亮度，最高250
#cap.set(11,250)#对比度，最高250
#cap.set(15,0)#曝光时间，最高0，普通-4
#cap.set(cv2.CAP_PROP_ISO_SPEED,0)
cv2.namedWindow('merged',-2)
for i in range(0,37):
    print (i,cap.get(23))
#print (cap.get(3))
while True:
    print (cap.get(10),cap.get(11),cap.get(12),cap.get(13),cap.get(14),cap.get(15),cap.get(16),cap.get(cv2.CAP_PROP_ISO_SPEED))
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,6)
    b,g,r=cv2.split(frame)
    #b,g,r=cv2.split(frame)
    b1=np.zeros((int(cap.get(4)),int(cap.get(3))), np.uint8)
    r=np.zeros((int(cap.get(4)),int(cap.get(3))), np.uint8)
    cv2.imshow('gray',gray)
    #cv2.imshow('gray+',gray*5)
    cv2.imshow('frame',frame)
    #merged = cv2.merge([b1,gray,r])
    #cv2.imshow('merged',merged)
#    cv2.imshow('b',b*3)
#    cv2.imshow('g',g*3)
#    cv2.imshow('r',r*3)
    cn=cv2.waitKey(1)
    if cn==ord('q'):
        print ('q')
        break
    elif cn==ord('s'):
        print ('s')
        cv2.imwrite('1.png',frame)
cv2.destroyAllWindows()
cap.release()
