import cv2
import numpy as np
import rect
image=cv2.imread('star.jpg')
x,y,z=image.shape
y1=640
x1=int(x/y*y1)
resize = cv2.resize(image, (y1, x1))
print (x1)
# resize image so it can be processed
# choose optimal dimensions such that important content is not lost
#image = cv2.resize(image, (y1, x1))
#resize=cv2.resize(image,
cv2.imshow('resize',resize)
gray=cv2.cvtColor(resize,6)
cv2.imshow('gray',gray)
#ret,thresh=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
#kernel = np.array([ [0,-1,0],[-1,5,-1],[0,-1,0] ],np.float32)   # kernel should be floating point type.
#filter2D = cv2.filter2D(frame,-1,kernel)
#cv2.imshow('filter2D',filter2D)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('blurred',blurred)
edged = cv2.Canny(blurred, 0, 100)
cv2.imshow('edged ',edged )
ret,contours,hierarchy = cv2.findContours(edged, cv2.RETR_TREE, 2)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
copy=resize.copy()
copy= cv2.drawContours(copy, contours, 0, (255,255,255), 2)
x,y,w,h = cv2.boundingRect(contours[0])
copy = cv2.rectangle(copy,(x,y),(x+w,y+h),(0,255,0),2)
#
#for cnt in contours:
#    print ('area is ',cv2.contourArea(cnt))
    
    #print (cv2.contourArea(contours()))
            
#    copy= cv2.drawContours(copy, cnt, -1, (255,255,255), 10)
#    print ('Max is ',cv2.contourArea(contours[0]))

cv2.imshow('image',copy)
cv2.imwrite('resize.jpg',copy)
p=cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], 0.02 * p, True)
print (approx.shape)
approx=approx.reshape(4,2)
#approx.astype(float)
#print (float32(1.3))
print (approx.dtype)
approx=np.float32(approx)
print (approx.dtype)
#
#float(approx )
#a1=rect.rectify(approx)
#print (p)
#print (approx.dtype)
#print (a1)
#pts2 = np.float32([[0,0],[800,0],[800,800],[0,800]])
pts2 = np.float32([[0,0],[800,0],[800,800],[0,800]])

print (pts2.shape)
print (pts2.ndim)
pts3 = np.float32([[0,0],[800,0],[800,800],[0,800]])

M = cv2.getPerspectiveTransform(approx,pts2)
dst = cv2.warpPerspective(resize,M,(800,800))
cv2.imshow('dst',dst)
cv2.waitKey(0)


