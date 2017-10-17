# -*- coding: cp936 -*-

#中文，你懂得
import cv2
import datetime
import easygui
from easygui import msgbox, multenterbox

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
                roi=img[int(y1*0.7):y1+int(y2*1.3), x1:x1+x2]
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
    faceCascade = cv2.CascadeClassifier('cars.xml')
    #人脸发现的xml路径， 发现是发现有没有人脸， 识别是识别是哪张脸不一样。
    print ('hello1')
    while cv2.waitKey(1)!=ord('q'):
        time=datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        #日期时间显示在左上角
        _,frame=cap.read()
        
        copy0=frame.copy()
        


        rects = faceCascade.detectMultiScale(copy0, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20,20))
        #print (len(rects))
  
        for x1, y1, x2, y2 in rects:
            
            cv2.rectangle(copy0, (x1, int(y1*0.7)), (x1+x2, y1+int(y2*1.3)), (127, 255, 0), 2)
            #roi=copy0[int(y1*0.7):y1+int(y2*1.3), x1:x1+x2]
            #cv2.imshow('roi',roi)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(copy0, logo, (600, 10), font, 0.5, (0, 0, 0), 1)
        cv2.putText(copy0, time, (0, 10), font, 0.5, (255, 255, 255), 1)
        cv2.putText(copy0, promotion, (0, 470), font, 0.5, (0, 0, 255), 1)
        cv2.imshow('output',copy0)
        if cv2.waitKey(1)==27:
            try:
                pressESC(copy0,rects)
    
    #尝试获得命令的第一个参数， 也就是图片的名字
            except:
                pass
            


    cap.release()
    cv2.destroyAllWindows()
    
