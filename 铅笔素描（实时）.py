import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while cv2.waitKey(1)!=27:
    ret,im=cap.read()
#gray=cv2.cvtColor(frame,6)
    dst_gray, dst_color = cv2.pencilSketch(im, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
#cv2.imshow('frame',frame)
    dst = cv2.stylization(im, sigma_s=60, sigma_r=0.07)
    cv2.imshow('dst_gray',dst_gray)
    cv2.imshow('dst_color',dst_color)
    cv2.imshow('dst',dst)
cv2.waitKey(0)
