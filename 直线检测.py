import cv2

import numpy as np

cap=cv2.VideoCapture(0)

while cv2.waitKey(10)!=27:

    _,frame=cap.read()

    gray=cv2.cvtColor(frame,6)

    blur=cv2.blur(gray,(5,5),0)

    edges = cv2.Canny(blur,50,150,apertureSize = 3)

    

    cv2.imshow('edges',edges)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 80, minLineLength=100, maxLineGap=10)

    copy=frame.copy()

    

    try:

        

        for line in lines:

            x1,y1,x2,y2=line.reshape(4)

            print (x1,y1,x2,y2)

            cv2.line(copy, (x1,y1), (x2,y2), (0,255,0), 3, 8)

        #print ('line0 is ',lines[0])

        #print ('line1 is ',lines[1])

    except:

        print ('no line found')

    #else:

    #    print ('else')

    cv2.imshow('frame',copy)

    if cv2.waitKey(1)==ord('s'):

        cv2.waitKey(0)

    

cap.release()

cv2.destroyAllWindows()
