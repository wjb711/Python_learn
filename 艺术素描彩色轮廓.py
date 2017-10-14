import cv2
import numpy as np
cap=cv2.VideoCapture(0)
cv2.namedWindow('output',0)
while cv2.waitKey(1)!=27:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,6)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh=50
    #edges = cv2.Canny(blur,thresh,thresh*2)
    edges = cv2.Canny(blur,0,50)
    drawing = np.zeros(frame.shape,np.uint8)
    #ret,contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    ret,contours,hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        color = np.random.randint(0,255,(3)).tolist()  # Select a random color
        cv2.drawContours(drawing,[cnt],0,color,2)
        cv2.imshow('output',drawing)
        cv2.imwrite('1.jpg',drawing)
    cv2.imshow('input',frame)
    #dst_gray, dst_color = cv2.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

cap.release()
cv2.destroyAllWindows()
