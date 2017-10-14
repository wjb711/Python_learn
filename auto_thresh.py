import cv2
cap=cv2.VideoCapture(0)
cn=cv2.waitKey(1)
while cn!=ord('q'):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,6)
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('th',th)
    cn=cv2.waitKey(1)
                    
