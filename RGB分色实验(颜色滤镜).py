import cv2
import numpy as np
im=cv2.imread('c2.png')
print ('shape is ',im.shape)
y,x,z=im.shape
im1=np.zeros((y,x,z),np.uint8)
#cv2.imshow('im1',im1)
b0=im[:,:,0]
g0=im[:,:,1]
r0=im[:,:,2]
b1=im1[:,:,0]
g1=im1[:,:,1]
r1=im1[:,:,2]
b01=cv2.merge((b0,g1,r1))
g01=cv2.merge((b1,g0,r1))
r01=cv2.merge((b1,g1,r0))


cv2.imshow('b01',b01)
cv2.imshow('g01',g01)
cv2.imshow('r01',r01)
cv2.imshow('im',im)
cv2.waitKey(0)
