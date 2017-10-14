import cv2
import numpy as np
'''
原理：摄像头分三色光，蓝，绿，红
其中暗光环境中，绿色最为敏感，所以我们把绿色分离出来，做加强
'''
cap=cv2.VideoCapture(0)
cap.set(3,3000)
cap.set(4,3000)
cap.set(15, 2.0)
dict={}
i=0
#夜光放大倍数
x=20
while True:
    _,frame=cap.read()
    #分离三色光
    b,g,r=cv2.split(frame)
    #b=np.zeros(480,640)
    #b=np.zeros((480,640), np.uint8)
    #r=np.zeros((480,640), np.uint8)
    #merged = cv2.merge([b,g+g0,r])
    
    #cv2.imshow('frame',frame)
    #cv2.imshow('b',b)
    cv2.imshow('frame',frame)
    #cv2.imshow('merged',merged)
    
    #cv2.imshow('r',r)
    dict[i]=g
    sum=np.zeros((480,640), np.uint8)
    #把绿光加强，就是吧前面几帧的内容叠加在乘以放大倍数
    if i>x:
        for y in [i-x,i]:
            sum=sum+dict[y]
            merged = cv2.merge([b,sum*x,r])
            cv2.imshow('merged',merged)
    #print (dict)
    i=i+1
    cv2.waitKey(1)
