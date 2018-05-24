import cv2,_thread
import datetime,time
import numpy as np
import winsound
#import winsound
def print_time( threadName, delay):
   global mode
   #print ('mode',mode)
   
   try:
      if mode==True:
         print ('skip')
         pass
      else:
         mode=True
         #print (mode)
         time.sleep(1)
         winsound.Beep(600,200)
         print (1)
         
         mode=False
   except:
      mode=True
      #winsound.Beep(600,500)
      time.sleep(1)
      print (0)
      #print (mode)
      winsound.Beep(600,200)
      mode=False
      
def beep():
   pass
    #winsound.Beep(600,500)

def nothing(x):
    pass

params = cv2.SimpleBlobDetector_Params()
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('minArea','image',150,3000,nothing)
cv2.createTrackbar('Circularity','image',1,10,nothing)
cv2.createTrackbar('Convexity','image',1,10,nothing)
cv2.createTrackbar('InertiaRatio','image',1,10,nothing)
cv2.createTrackbar('white','image',180,255,nothing)
    
cap=cv2.VideoCapture(0)
while True:
    #print (datetime.datetime.now())
   minArea = cv2.getTrackbarPos('minArea','image')
   Circularity = cv2.getTrackbarPos('Circularity','image')/10
   Convexity = cv2.getTrackbarPos('Convexity','image')/10
   InertiaRatio = cv2.getTrackbarPos('InertiaRatio','image')/10
   white = cv2.getTrackbarPos('white','image')
   _,frame=cap.read()

   copy0=frame.copy()
   cv2.rectangle(copy0,(175,100),(440,345),(0,255,0),3)
   copy=frame
   roi=frame[100:345, 175:440]
    
    #gray=cv2.cvtColor(frame,6)
    #font = cv2.FONT_HERSHEY_SIMPLEX
    
    
    #cv2.imshow('gray',gray)
    #print(frame[0,0][1])
    #white=100
    #if frame[0,0][1]>white and frame[0,639][1]>white and frame[479,0][1]>white and frame[479,639][1]>0 and frame[240,320][1]>white:
        #cv2.putText(frame,'white',(20,20), 0, 0.8,(255,255,255),2,cv2.LINE_AA)
    
   params.minThreshold = 10;
   params.maxThreshold = 200;

   # Filter by Area.
   params.filterByArea = True
   params.minArea = minArea

   # Filter by Circularity
   params.filterByCircularity = True
   params.minCircularity = Circularity

   # Filter by Convexity
   params.filterByConvexity = True
   params.minConvexity = Convexity

   # Filter by Inertia
   params.filterByInertia = True
   params.minInertiaRatio = InertiaRatio
   detector = cv2.SimpleBlobDetector_create(params)
   keypoints = detector.detect(roi)
   #print (keypoints)
   roi=cv2.drawKeypoints(roi, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
##        #print (frame[0,0][1])
   if keypoints==[]:
      cv2.putText(copy0,'Pass',(50,50), 0, 2,(0,255,0),2,cv2.LINE_AA)
##            
##        else:
##            cv2.putText(frame,'Fail',(20,20), 0, 0.8,(0,0,255),2,cv2.LINE_AA)
      
##            #time.sleep(1)
##            
##        #print ('yes')
   else:
      print (keypoints)
      cv2.putText(copy0,'Fail',(50,50), 0, 2,(0,0,255),2,cv2.LINE_AA)
      _thread.start_new_thread(print_time, ("Thread-1", 2, ))
   cv2.imshow('roi',roi)
   copy0[100:345, 175:440]=roi
   key=cv2.waitKey(1)
   if key==27:
      break
   cv2.imshow('image',copy0)
##    cv2.imshow('0',copy)
cv2.destroyAllWindows()
