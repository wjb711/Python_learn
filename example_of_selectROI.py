# -*- coding: cp936 -*-
#中文，你懂得
'''
selectROI是contrib模块中的一个内容， 最近新增到opencv
关于如何安装配置contrib模块， 请参见我的安装配置指导
'''
import cv2
#import numpy as np
cap=cv2.VideoCapture(0)
#ret=cap.set(3,1280)
#ret=cap.set(4,720)
cv2.namedWindow('frame',0)

while cv2.waitKey(1)!=27:
    ret, frame=cap.read()
    
    #按空格键截图，截图后画框截图
    if cv2.waitKey(1)==ord(' '):
        (x1,y1,x2,y2)=cv2.selectROI('frame',frame,0,0)
        #selectROI输出4个值，是左上顶角的，x，y值， 以及之后的w, h值， 但注意是float需要转换为int
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        src=frame[y1:y1+y2,x1:x1+x2]
        #按回车或空格键，把截出来的图放大充满640x480的屏幕
        im=cv2.resize(src, (640, 480), interpolation = cv2.INTER_CUBIC)
        cv2.imshow('im',im)
        cv2.waitKey(1000)
    cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()
