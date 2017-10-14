import cv2,datetime
cap=cv2.VideoCapture(0)
d=0
e=0
ret=cap.set(15,-1)
ret=cap.set(3,2000)
ret=cap.set(4,2000)
while 1:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,6)
    ret,thresh = cv2.threshold(gray,3,250,cv2.THRESH_BINARY)
    cv2.imshow('hello',frame)
    
    c=frame
    d=cv2.add(d,thresh)
    e=cv2.add(e,gray)
    if cv2.waitKey(1)==ord('s'):
        now = datetime.datetime.now()
        im_name1=(now.strftime('%Y-%m-%d_%H%M%S')+'.jpg')
        im_name2=(now.strftime('%Y-%m-%d_%H%M%S')+'.png')
        cv2.imwrite(im_name1,d)
        cv2.imwrite(im_name2,e)
    cv2.imshow('d',d)
    cv2.imshow('e',e)
cap.release
cv2.destroyAllWindows()
