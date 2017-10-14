import cv2
cap=cv2.VideoCapture(0)
ret=cap.set(3,960)
ret=cap.set(4,720)

while(1):
    ret, frame=cap.read()
    cv2.imshow('1',frame)
    cv2.waitKey(20)
