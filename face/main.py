# -*- coding: cp936 -*-

#中文，你懂得
import cv2
import datetime
import easygui
from easygui import msgbox, multenterbox
import numpy as np
from PIL import Image
import pytesseract
def image_colorfulness(image): 
    #将图片分为B,G,R三部分（注意，这里得到的R、G、B为向量而不是标量） 
    (B, G, R) = cv2.split(image.astype("float")) 

    #rg = R - G
    rg = np.absolute(R - G) 

    #yb = 0.5 * (R + G) - B
    yb = np.absolute(0.5 * (R + G) - B) 

    #计算rg和yb的平均值和标准差
    (rbMean, rbStd) = (np.mean(rg), np.std(rg)) 
    (ybMean, ybStd) = (np.mean(yb), np.std(yb)) 

    #计算rgyb的标准差和平均值
    stdRoot = np.sqrt((rbStd ** 2) + (ybStd ** 2))
    meanRoot = np.sqrt((rbMean ** 2) + (ybMean ** 2)) 

    # 返回颜色丰富度C 
    return stdRoot + (0.3 * meanRoot)

#image = cv2.imread('图片路径') 
#print(image_colorfulness(image))

#导入各个模块
def pressESC(img,rect):
#自定义按了esc键后发生的事件，此处调用了easybox
    cv2.imwrite('pic.jpg',img)
    image = 'pic.jpg'
        
    msg = "是否加入到人脸识别库中?"
    choices = ["Yes","No","退出程序"]
    reply = easygui.buttonbox(msg, image=image, choices=choices)
    if reply=="Yes" or reply=='pic.jpg':
        print (reply)
        if len(rect)==1:
        
            flavor = easygui.enterbox("请输入名字（必须是英文（拼音），不能有空格和特殊符号）") 
            easygui.msgbox ("您输入了： " + flavor)
            folder='raw'
            name=folder+"/"+flavor+'.jpg'
            #easygui.msgbox (name)
            cv2.imwrite(name,img)
            for x1, y1, x2, y2 in rects:
            
            #cv2.rectangle(copy0, (x1, int(y1*0.7)), (x1+x2, y1+int(y2*1.3)), (127, 255, 0), 2)
                roi=img[y1:y1+y2, x1:x1+x2]
                folder1='faces'
                name1=folder1+"/"+flavor+'.jpg'
                cv2.imwrite(name1,roi)
            #print (roi)
        else:
            easygui.msgbox ('没有人脸或不止一张脸，请确保单人拍照')

    elif reply=="No" or reply==None:
        print (reply)
        pass
    #elif reply=='pic.jpg':
    #    flavor = easygui.enterbox("请输入名字（必须是英文（拼音），不能有空格和特殊符号）") 
    #    easygui.msgbox ("您输入了： " + flavor)
    else:
        print ('reply is ',reply)
        cap.release()
        cv2.destroyAllWindows()
        
if __name__ == "__main__":
#主函数

    logo='GD'
    #右上角的图标
    promotion='press ESC'
    #最下角的提示

    cap=cv2.VideoCapture(0)
    cv2.namedWindow('output',0)
    print ('hello')
    #faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #faceCascade = cv2.CascadeClassifier('C:\\temp\\pos2\\dt\\cascade.xml')
    faceCascade = cv2.CascadeClassifier('C:\\temp\\pos2\\dt\\car_plate.xml')
    #人脸发现的xml路径， 发现是发现有没有人脸， 识别是识别是哪张脸不一样。
    print ('hello1')
    cap.set(3,1280)
    cap.set(4,960)
    while cv2.waitKey(1)!=ord('q'):
        time=datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        #日期时间显示在左上角
        #_,frame=cap.read()
        frame=cv2.imread('a8.jpg')
        
        copy0=frame.copy()
        


        #rects = faceCascade.detectMultiScale(copy0, 1.1, 2, cv2.CASCADE_SCALE_IMAGE, (20,20))
        rects = faceCascade.detectMultiScale(copy0, 1.1, 3, 0)
        #print (len(rects))
  
        for x1, y1, x2, y2 in rects:
            
            #cv2.rectangle(copy0, (x1, y1), (x1+x2, y1+y2), (127, 255, 0), 2)
            roi=frame[y1:y1+y2, x1:x1+x2]
            
            #cv2.imwrite('a4.jpg',roi)
            value=image_colorfulness(roi)
            #print (value)
            if value >10:
                cv2.rectangle(copy0, (x1, y1), (x1+x2, y1+y2), (127, 255, 0), 2)
                #print (value)
                image = Image.fromarray(cv2.cvtColor(roi,cv2.COLOR_BGR2RGB)) 
                #chepai=pytesseract.image_to_string(image,lang = 'chepai')
                #print (chepai)
                #print ('len is ',len(chepai))
                #if '赣' in chepai:
                #    print ('yes, 赣 in chepai')
                #    chepai=chepai.replace(' ','')
                #    n=chepai.find('赣')
                #    if n>=0:
                #        label=chepai[n:n+7]
                #        print ('label is: ',label)
                #        cv2.imshow('output',copy0)
                #        input('any key to continue:')
                #if chepai=='赣F16712':
                #    #print ('yes',len(chepai))
                #    pass
                #print ('done')
                resize=cv2.resize(roi,(300,150))
                copy0[0:150,0:300]=resize
                cv2.imshow('output',copy0)
                cv2.imshow('resize',resize)
                #cv2.imshow('roi',resize)
                #input('a')
                #cv2.imwrite('a4.jpg',roi)
                #font = cv2.FONT_HERSHEY_DUPLEX
        #cv2.putText(copy0, logo, (600, 10), font, 0.5, (0, 0, 0), 1)
        #cv2.putText(copy0, time, (0, 10), font, 0.5, (255, 255, 255), 1)
        #cv2.putText(copy0, promotion, (0, 470), font, 0.5, (0, 0, 255), 1)
        
        if cv2.waitKey(1)==27:
            try:
                break
                #pressESC(copy0,rects)
    
    #尝试获得命令的第一个参数， 也就是图片的名字
            except:
                pass
            


    cap.release()
    cv2.destroyAllWindows()
    
