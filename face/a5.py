import cv2
faceCascade = cv2.CascadeClassifier('C:\\temp\\pos2\\dt\\cascade.xml')
while cv2.waitKey(1)!=ord('q'):
    #time=datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        #日期时间显示在左上角
        #_,frame=cap.read()
    frame=cv2.imread('a5.jpg')
    copy0=frame.copy()
    
    rects = faceCascade.detectMultiScale(frame, 1.2, 10, 0)

    for x1, y1, x2, y2 in rects:
        
        #cv2.rectangle(copy0, (x1, y1), (x1+x2, y1+y2), (127, 255, 0), 2)
        roi=frame[y1:y1+y2, x1:x1+x2]
        cv2.rectangle(copy0, (x1, y1), (x1+x2, y1+y2), (127, 255, 0), 2)
    cv2.imshow('1',copy0)
