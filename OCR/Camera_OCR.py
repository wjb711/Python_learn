import cv2,datetime,os
import numpy as np
from aip import AipOcr
import easygui

def baidu_ocr():
    APP_ID = '10839731';
    API_KEY = '93THkmKKFHGS5inBt8ulCeGH';
    SECRET_KEY = 'EVUeKdmNuCZFyD7xqx0Pr6FLWYyZENvo'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image=open('t.png','rb').read()
    t=client.basicGeneral(image);

    """ 如果有可选参数 """

    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    print (t)
    print (t['words_result'])
    sum0=''
    for i in t['words_result']:
        sum0=sum0+i['words']+'\n'
    print (sum0)
    easygui.msgbox(sum0)
    cv2.destroyWindow('ROI')
    os.remove('t.png')
    
def nothing(event,x,y,flags,param):
    #print (event,flags)
    x1,y1=x,y
    global x0,y0,mode
    if event==1:
        mode=True
        #img0=frame.copy()
        x0,y0=x,y
       # cv2.imshow('2',img0)

       
    if flags==1:
        #img0=img1.copy()
        roi=img0[y0:y, x0:x]
        cv2.imshow('5',roi)
        
        #baidu_ocr()
        
    if event==4:
        roi=img0[y0:y, x0:x]
        cv2.imshow('ROI',roi)
        cv2.imwrite('t.png',roi)
        baidu_ocr()
        mode=False
os.environ['https_proxy']='http://wanjianb:Beijing123_@web-gate4a.accounts.intern:3128'
cv2.namedWindow('OCR')

cv2.setMouseCallback('OCR',nothing)
cap=cv2.VideoCapture(1)
mode=False
while True:
    if mode==False:
        _,frame=cap.read()
        cv2.imshow('OCR',frame)
        cv2.waitKey(1)

    else:
        mode=True
        img0=frame.copy()
        cv2.imshow('OCR',img0)
        cv2.waitKey(1)
    #print ('mode is:',mode)
