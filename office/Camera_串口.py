#图形追踪程序，原理是通过opencv抓取一个图片样例， 然后在摄像头里通过模板追踪， 最后对追踪到的结果做图片比对， 图片比对的值符合要求的， 画出框来
#按q键退出， 按空格键开始截图，回车结束截图

import cv2 #opencv的包
from skimage.measure import compare_ssim
import imutils
import numpy as np
import os
import easygui as g
import serial
  #端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
portx="COM4"
  #波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
bps=9600
  #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex=5
  # 打开串口，并得到串口对象
ser=serial.Serial(portx,bps,timeout=timex)

  # 写数据
print(ser.name)
print (ser.port)
print (ser.baudrate) #波特率
print (ser.bytesize) #字节大小
print (ser.parity) #校验位N－无校验，E－偶校验，O－奇校验
print (ser.stopbits) #停止位
print (ser.timeout) #读超时设置
print (ser.writeTimeout) #写超时
print (ser.xonxoff) #软件流控
print (ser.rtscts) #硬件流控
print (ser.dsrdtr) #硬件流控
print (ser.interCharTimeout) #字符间隔超时

d0=bytes.fromhex('A0 01 00 A1')
d1=bytes.fromhex('A0 01 01 A2')

#图形比对的包

if os.path.exists('template.jpg'):
    pass
    #template = cv2.imread('template.jpg',0)
    #print('if:')
    #print(template.shape)
else:
    #print('except:')
    template = np.zeros((100,100))
#初始化时需要一张template.jpg的图片，放在同一目录，任意图片都可
    #template.fill(255)
    #print(template.shape)
    cv2.imwrite('template.jpg',template)
    #template = cv2.imread('template.jpg',0)
template = cv2.imread('template.jpg',0)
capture = cv2.VideoCapture(0)
#打开摄像头

#capture.set(3,800) #设置分辨率

#capture.set(4,600)
cv2.namedWindow('Camera_Compare',0)
#定义窗口名称， 可以最大化

while(True):
    try:
    
        # 获取一帧
        ret, frame = capture.read()
        # 将这帧转换为灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



        #cv2.imshow('frame', gray)
        key=cv2.waitKey(1)
        if key == ord('q') or key == 27:
        #    print('q')
            break
        if key == ord('h'):
            #print('h')
            help_text='''
    欢迎使用本程序
    本程序的目的是通过计算机视觉，实现物品追踪，和图片相似度比对
    调出帮助文件：鼠标选中窗口，按h键，
    屏幕追踪：鼠标选中窗口，按空格键，开始屏幕截图，使用鼠标左键拖拽画出要追踪物品的蓝框，再按空格键结束截图
    退出：鼠标选中窗口，按q键或[ESC]键
    附：
    计算机视觉与光线有关， 建议使用强光照射避免误差
    也与物品角度有关， 物品有前后如有倾斜，较多过大，也无法正常识别
    本程序默认使用计算机默认的第一个摄像头， 如笔记本电脑需要调用第二个USB摄像头， 需要将源码中
    capture = cv2.VideoCapture(0) 改为
    capture = cv2.VideoCapture(1)
    '''
            
            g.msgbox(help_text)
        if key == ord('s'):
            #print('s')
            cv2.imwrite('1.jpg',frame)
        if key == ord(' '):
        #按空格键截取第一个模板的图，也就是要框出追踪的图形，回车结束截图
            g.msgbox('请在窗口中拖拽鼠标左键截取要追踪的物品图片')
            (x1,y1,x2,y2)=cv2.selectROI('Camera_Compare',frame,0,0)
            x1=int(x1)
            x2=int(x2)
            y1=int(y1)
            y2=int(y2)
            src=gray[y1:y1+y2,x1:x1+x2]
            template=src
            cv2.imwrite('template.jpg',template)


        #img = cv2.imread('1.jpg',0)
        img0=frame.copy()
        img=gray.copy()
        
        #print(template.shape)
        w, h = template.shape[::-1]
        #读出模板宽度和高度

        
        methods = ['cv2.TM_CCOEFF_NORMED']
        # 6种模板匹配模式， 我们这里选择TM_CCOEFF_NORMED， 也可以选其他的 'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED'

        for meth in methods:
            #img = img2.copy()
            method = eval(meth)

            # Apply template Matching
            res = cv2.matchTemplate(img,template,method)
            #做匹配
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            top_left = max_loc
            #获取匹配图形左上角的坐标
            bottom_right = (top_left[0] + w, top_left[1] + h)
            #匹配图形区域的坐标
            roi=img[top_left[1]:top_left[1]+h,top_left[0]:top_left[0]+w]
            #匹配后的图形
            (score,diff) = compare_ssim(template,roi,full = True)
            #拿模板和匹配后的图形做图形比对，值的区间为0-1， 1为最像，0为最不像， 一般都是一个小数值
            diff = (diff *255).astype("uint8")
            #print("相似度:{}".format(score),score)
            font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.imshow('roi',roi)
            if score >0.6:
                ser.write(d1)
                #设定相似度最低值
                font = cv2.FONT_HERSHEY_SIMPLEX
                imgzi = cv2.putText(img0, 'scroe:'+str(score)[:5], (300, 20), font, 1, (255, 255, 255), 2)
                if score >0.85:
                    cv2.rectangle(img0,top_left, bottom_right, (0,255,0), 2)
                else:
                    cv2.rectangle(img0,top_left, bottom_right, (0,0,255), 2)
                #如果相似画出框来
            else:
                ser.write(d0)
            imgzi = cv2.putText(img0, 'Press h for help', (5, 20), font, 1, (0, 0, 0), 2)
            cv2.imshow('Camera_Compare',img0)
    except:
        pass
cv2.destroyAllWindows()
