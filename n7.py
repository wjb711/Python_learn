# -*- coding:utf-8 -*-
__author__ = 'Microcosm'

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# 获取第一帧
ret,frame = cap.read()
print (frame.shape)
# 设置初始跟踪对象的窗口大小
#r,h,c,w = 120,100,253,100
r,h,c,w = 180,80,140,90
track_window = (c,r,w,h)

cv2.rectangle(frame,(c,r),(c+w,r+h),255,2)
cv2.imshow("frame",frame)
cv2.waitKey(0)
# 设置感兴趣的区域
roi = frame[r:r+h,c:c+w]
#cv2.imshow("roi",roi)
#cv2.waitKey(0)
hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0.,0.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180 ])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while(True):
    ret, frame = cap.read()

    if ret is True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # 调用meanshift获取新的位置
        ret,track_window = cv2.meanShift(dst,track_window,term_crit)

        # 画出它的位置
        x,y,w,h = track_window

        cv2.rectangle(frame,(x,y),(x+w,y+h),255,2)
        cv2.imshow("frame",frame)

        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        #else:
        #    cv2.imwrite(chr(k)+".jpg",frame)

    else:
        break

cv2.destroyAllWindows()
cap.release()
