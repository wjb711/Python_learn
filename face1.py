# -*- coding: cp936 -*-

#中文，你懂得

# import the necessary packages

from imutils import face_utils

import numpy as np

import dlib

import cv2

#加载若干的模块

detector = dlib.get_frontal_face_detector()

#detector这个用来发现人脸， 几张人脸

predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#   You can get the shape_predictor_68_face_landmarks.dat file from:
#   http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

#发现人脸的细节，眼睛嘴巴，眉毛等。

image=cv2.imread('2008.jpg')

#读取图片

gray=cv2.cvtColor(image,6)

#转灰度

rects = detector(gray, 1)

#开始读图取人脸了

#print (rects)

for (i, rect) in enumerate(rects):

#i是人脸数量， rects是集合， rect是单张人脸的方框

    #print (i,rect)

    shape = predictor(gray, rect)

    #每张人脸取细节

    #print (shape)

    shape = face_utils.shape_to_np(shape)

    #转换为opencv的xy点数值，共68个

    #print (shape)

    for (x, y) in shape:

        cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

        #用红笔画点，每张脸共68个点

cv2.imshow("Output", image)

#输出图像

cv2.waitKey(0)
