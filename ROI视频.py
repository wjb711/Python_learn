import cv2,time,datetime
import numpy as np
def draw_circle(event,x,y,flags,param):
    print (event,x,y,flags,param)
    if event==1:
        #img0 = np.zeros((480,640), np.uint8)
        #img0a = np.zeros((480,640,3), np.uint8)
        #img255 = np.ones((480,640), np.uint8)*255
        im=frame
        copy=frame.copy()
        r = cv2.selectROI(im)
        imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        img255[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]=0
        img0[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]=255
        img0a[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]=imCrop
        #cv2.imshow("Image", imCrop)
        #cv2.imshow("Image3", img0a)
        #time.sleep(5)
        #
        cv2.destroyWindow('ROI selector')
        #img1_bg = cv2.bitwise_and(frame,frame,mask = img255)
        
        #cv2.destroyWindow('Image')
    pass
img0 = np.zeros((480,640), np.uint8)
img0a = np.zeros((480,640,3), np.uint8)
img255 = np.ones((480,640), np.uint8)*255
#cv2.imshow('img0',img0)
#cv2.imshow('img255',img255)
cap=cv2.VideoCapture(0)
cv2.namedWindow('1',cv2.WINDOW_NORMAL)
cv2.namedWindow('Image4',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Image4',draw_circle)
while True:
    _,frame=cap.read()
    img1_bg = cv2.bitwise_and(frame,frame,mask = img255)
    img2_bg = cv2.bitwise_and(frame,frame,mask = img0)
    
    #cv2.imshow("Image1", img1_bg)
    #cv2.imshow("Image2", img2_bg)
    #cv2.imshow('1',frame)
    dst = cv2.add(img1_bg,img0a)
    cv2.imshow("Image4", dst)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    if key==ord('n'):
        img0 = np.zeros((480,640), np.uint8)
        img0a = np.zeros((480,640,3), np.uint8)
        img255 = np.ones((480,640), np.uint8)*255
    if key==ord('s'):
        print ('save')
        now=str(datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S"))
        print (now)
        cv2.imwrite(now+'.jpg',dst)
        print (now+'.jpg')
        time.sleep(2)
        
cv2.destroyAllWindows()
    #im = cv2.imread("image.jpg")
    #im=frame

    # Select ROI
    #r = cv2.selectROI(im)

    # Crop image
    #imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    # Display cropped image
    #cv2.imshow("Image", imCrop)
    #cv2.imshow("Image", imCrop)
    #cv2.waitKey(0)
