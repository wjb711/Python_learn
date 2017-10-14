#我们来研究下通过数组的基本操作，实现图像的一些变换
import cv2,time
import numpy as np
img=cv2.imread('timg.jpg')
#实例1，最简单，新的图像和原图一致
yizhi=img
cv2.imshow('yizhi',yizhi)
cv2.imshow('img',img)
#实例2，做镜像左右翻转
zuoyou=np.zeros(img.shape,np.uint8)
x=img.shape[0]
y=img.shape[1]
for i in range(0,x):
    for s in range(0,y):
        zuoyou[i,s]=img[i,y-1-s]
cv2.imshow('img',img)
cv2.imshow('zuoyou',zuoyou)
#实例3，镜像上下翻转
shangxia=np.zeros(img.shape,np.uint8)
x=img.shape[0]
y=img.shape[1]
for i in range(0,x):
    for s in range(0,y):
        shangxia[i,s]=img[x-1-i,s]
cv2.imshow('img',img)
cv2.imshow('shangxia',shangxia)
#实例4，上下左右都翻转
shangxiazuoyou=np.zeros(img.shape,np.uint8)
x=img.shape[0]
y=img.shape[1]
for i in range(0,x):
    for s in range(0,y):
        shangxiazuoyou[i,s]=img[x-1-i,y-1-s]
cv2.imshow('img',img)
cv2.imshow('shangxiazuoyou',shangxiazuoyou)
#实例5，点状图
dianzhuangtu=np.ones(img.shape,np.uint8)*255
#此为白底，如黑底为dianzhuangtu=np.zeros(img.shape,np.uint8)
x=img.shape[0]
y=img.shape[1]
for i in range(0,x,2):
    for s in range(0,y,2):
        dianzhuangtu[i,s]=img[i,s]
cv2.imshow('img',img)
cv2.imshow('dianzhuangtu',dianzhuangtu)

#实例6，缩小3倍
suoxiao=np.zeros(img.shape,np.uint8)
x=img.shape[0]
y=img.shape[1]
n=5
#n为缩小倍数
for i in range(0,int(x/n)):
    for s in range(0,int(y/n)):
        suoxiao[i,s]=img[i*n,s*n]
cv2.imshow('img',img)
cv2.imshow('suoxiao',suoxiao)

#实例7，缩放图片(可缩可放)
n=1.5
#n为缩放系数，大于1为放大，小于1为缩小，不可为负数或0
suofang=np.zeros((int(img.shape[0]*n),int(img.shape[1]*n),3),np.uint8)
x=img.shape[0]
y=img.shape[1]

#n为放大倍数
for i in range(0,int(x*n)):
    for s in range(0,int(y*n)):
        suofang[i,s]=img[int(i/n),int(s/n)]
cv2.imshow('img',img)
cv2.imshow('suofang',suofang)

#实例8，从上往下逐行显示图片
zhuhang=np.zeros(img.shape,np.uint8)
x=img.shape[0]
y=img.shape[1]
for i in range(0,x):
    zhuhang[i]=img[i]
    cv2.imshow('zhuhang',zhuhang)
    cv2.waitKey(10)
cv2.imshow('img',img)


#实例9，从上往下逐行显示图片
zhuhang2=np.zeros(img.shape,np.uint8)
x=img.shape[0]
y=img.shape[1]
for i in range(0,y):
    zhuhang2[:,i]=img[:,i]
    cv2.imshow('zhuhang2',zhuhang2)
    cv2.waitKey(10)
cv2.imshow('img',img)

