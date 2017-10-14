# -*- coding: cp936 -*-
#中文，你懂得
'''
#我女儿喜欢看小马宝莉，也喜欢给简笔画涂色彩
#我这个脚本就是给她写的， 随意找张动画片屏幕截图， 就可以制成简笔画了
#用法python pan_painting.py  你的图片 例如 python pan_painting.py  time.jpg
#此脚本是windows环境python 2.7+opencv3.2版本的， 配置见下面的链接
https://github.com/wjb711/Opencv_learning/blob/master/windows_python2.7_opencv3.2%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E6%8C%87%E5%AF%BC.txt
#需要提前安装speech模块， 安装方法pip install speech
如提示如下错误
no module named win32com.client错误解决
请下载对应pywin32插件
https://sourceforge.net/projects/pywin32/files/pywin32/
到这里下载微软tts
http://www.microsoft.com/en-us/download/confirmation.aspx?id=27224
'''

import cv2
#导入cv2这个module模块
import numpy as np
#导入numpy这个计算用的模块
#import argparse
#导入参数模块
import sys
#import speech
#加载语音模块

def draw_circle(event,x,y,flags,param):
    #global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if mode==True:
                
            print (x,y)
        else:
            print (y,x)
def nothing(x):
    pass
#自定义一个nothing的模块， 后面的trackbar动作会用到

import datetime

if __name__ == '__main__':
#如果是其他脚本调用，不执行下面的命令
    print(__doc__)
    #显示前面绿色的声明的内容

    try:
        fn = sys.argv[1]
        #尝试获得命令的第一个参数， 也就是图片的名字
    except:
        fn = 'images/time.jpg'
        print (fn)
        #如果找不到上面指定的图片名称， 默认名称为time.jpg
    mode=1
    #自定义一个模式,按m键切换原图,效果图


#speech.say("现在开始")
#说话， 代表开始
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,help="path to the input image")
#提示需要加入图片的提示
#args = vars(ap.parse_args())
#这个就是会代入程序的图片名称参数值

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
    im = cv2.imread(fn)
#读取命令中代入的图片名称
    kernel = np.ones((5,5),np.uint8)
#im=cv2.imread('time.jpg',0)
    res = cv2.resize(im,(1280, 960), interpolation = cv2.INTER_CUBIC)
#把原图调整到适合屏幕的1280x960
#cv2.imshow('原图',im)

    gray=cv2.cvtColor(res,6)
#把彩色图片黑吧=白灰度化
    res1=cv2.resize(gray,(256, 192), interpolation = cv2.INTER_CUBIC)
#把黑白后的原图缩小尺寸， 放到屏幕左上角， 做原图显示用

    cv2.namedWindow('简笔画',0)
#创建一个名字叫edge的新窗口，用来显示加工后的效果图， 0的意思是， 窗口可伸缩
    cv2.createTrackbar('阀值', '简笔画', 203, 255, nothing)
    cv2.createTrackbar('翻转', '简笔画', 2, 2, nothing)
    cv2.createTrackbar('角度', '简笔画', 0, 360, nothing)
#创建一个叫做thrs1的滑动条，默认值是127， 在0-255的范围内， 手动调整阀值范围， 调用上面的nothing模块，其实相当于什么都没做，这是格式要求的。
    while(True):
#循环，为什么要循环？因为手动调整阀值，效果跟着变，不停地调整，不停的变，所以要循环
        thrs1 = cv2.getTrackbarPos('阀值', '简笔画')
        thrs2 = cv2.getTrackbarPos('翻转', '简笔画')
        thrs3 = cv2.getTrackbarPos('角度', '简笔画')
    #print thrs1
    #阀值thrs1等于edge窗口中thrs1的值
        ret, thresh=cv2.threshold(gray,thrs1,255,cv2.THRESH_BINARY_INV)
    #
    #黑白差值化,标准取自滑动条上的阀值
    #cv2.imshow('thresh',thresh)
    #显示黑白差值图
        edges = cv2.Canny(thresh,0,255,3)
    #这个是边缘图，黑底，白线
        edges_INV =cv2.bitwise_not(edges)
    #取反， 白底，黑线
    #erosion = cv2.erode(edges1,kernel,iterations = 1)
    #dilation = cv2.dilate(edges1,kernel,iterations = 1)
    #cv2.imwrite(sys.argv[1]+'.jpg',edges_INV)
    #写入源文件， 替换掉原图
        edges_INV[0:192,0:256]=res1
    #左上角256x192部分等于上面的缩小的灰度原图
        flipped = cv2.flip(edges_INV,thrs2) #水平，垂直，以及水平垂直翻转
        M = cv2.getRotationMatrix2D((640,480),thrs3,1)#旋转缩放矩阵：(旋转中心，旋转角度，缩放因子)
        rotated = cv2.warpAffine(flipped ,M,(1280,960))#（原图， 收放指数， 如上， 最终大小）

        cv2.imshow('简笔画',rotated )

    #显示新图
        cn=cv2.waitKey(5)
        if cn==27:
            break

        if cn==ord('m'):
            print ('m')
            mode = not mode
            print (mode)
            if mode==True:
                edges_INV=res
                cv2.imshow('简笔画1',res)
            

        if cn==ord(' '):
            #cv2.imwrite('time1.jpg',edges_INV)
            now = datetime.datetime.now()
            #print ("yes")
            im_name1=(now.strftime('%Y-%m-%d_%H%M%S')+'.jpg')
            cv2.imwrite(im_name1,edges_INV)

    cv2.destroyAllWindows()
#cv2.imshow('erosion',erosion)
#cv2.imshow('dilation',dilation)
#speech.say("转换结束")
#语音提示， 提示程序完成
#cv2.waitKey(0)
#按任意键退出

