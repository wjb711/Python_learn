# -*- coding: cp936 -*-
import cv2
import numpy as np
import time
import sys
import datetime
img1=cv2.imread('1.jpg')
img2=cv2.imread('2.jpg')

diff = cv2.absdiff(img1, img2)
cv2.imshow('1',img1)
cv2.imshow('2',img2)
cv2.imshow('diff',diff)
cv2.waitKey(0)
        
