import cv2
import numpy as np
from PIL import Image
a=cv2.imread("a5.jpg")
imYcc=cv2.cvtColor(a,cv2.COLOR_BGR2YCR_CB)
cv2.imshow('a',a)

print (imYcc[39,50])
h=40
w=157
for i in range(h):
    for j in range(w):
        if imYcc[i,j][0]>0:
            imYcc[i,j][0]=0
        if imYcc[i,j][1]>0:
            imYcc[i,j][1]=0
            
        if 120<imYcc[i,j][2]<140:
            pass
        else:
            imYcc[i,j][2]=0
        pass
cv2.imshow('imYcc',imYcc)
cv2.imwrite('ok.jpg',imYcc)
im= Image.open("ok.jpg")
im.save("ok.jpg", dpi=(70,70))
