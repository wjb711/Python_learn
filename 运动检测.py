import numpy as np
import cv2

cap = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

fgbg =cv2.createBackgroundSubtractorKNN(history = 20, dist2Threshold=2000,detectShadows=1)

while(1):
    ret, frame = cap.read()
    cv2.imshow('frame0',frame)

    fgmask = fgbg.apply(frame)
    cv2.imshow('frame1',fgmask)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame2',fgmask)
    bitwise=cv2.bitwise_and(frame,frame,mask=fgmask)
    cv2.imshow('bitwise',bitwise)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
