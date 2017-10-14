import cv2
import numpy as np
import datetime
all=np.zeros((480*2,640*2,3),np.uint8)
print (all.shape)
cap=cv2.VideoCapture(0)
while cv2.waitKey(1)!=27:
    _,frame=cap.read()
    enhance = cv2.detailEnhance(frame, sigma_s=10, sigma_r=0.15)
    color = cv2.applyColorMap(enhance, 9)
    laplacian=cv2.Laplacian(enhance,cv2.CV_64F,ksize = 3)
    all[0:480,0:640]=frame
    all[0:480,640:1280]=enhance
    all[480:960,0:640]=color
    all[480:960,640:1280]=laplacian
    cv2.imshow('QA',all)
    if cv2.waitKey(1)==ord(' '):
        print ('yes')
        now = datetime.datetime.now()
        im_name1=(now.strftime('%Y-%m-%d_%H%M%S')+'.jpg')
        cv2.imwrite(im_name1,all)
        cv2.waitKey(3000)
        
    #cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()
