import cv2
import numpy as np
img = cv2.imread('hamper.jpg')
lower_reso = cv2.pyrDown(img)
cv2.imshow('1',lower_reso)
cv2.imshow('raw',img)
cv2.waitKey(0)

