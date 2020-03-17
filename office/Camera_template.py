#图形追踪程序，原理是通过opencv抓取一个图片样例， 然后在摄像头里通过模板追踪， 最后对追踪到的结果做图片比对， 图片比对的值符合要求的， 画出框来
#按q键退出， 按空格键开始截图，回车结束截图

import cv2 #opencv的包
from skimage.measure import compare_ssim
import imutils
#图形比对的包


template = cv2.imread('template.jpg',0)
#初始化时需要一张template.jpg的图片，放在同一目录，任意图片都可


capture = cv2.VideoCapture(0)
#打开摄像头

#capture.set(3,800) #设置分辨率

#capture.set(4,600)
cv2.namedWindow('hello',0)
#定义窗口名称， 可以最大化

while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    #cv2.imshow('frame', gray)
    key=cv2.waitKey(1)
    if key == ord('q'):
        print('q')
        break
    if key == ord('s'):
        print('s')
        cv2.imwrite('1.jpg',frame)
    if key == ord(' '):
    #按空格键截取第一个模板的图，也就是要框出追踪的图形，回车结束截图
        print('请截图')
        (x1,y1,x2,y2)=cv2.selectROI('hello',frame,0,0)
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        src=gray[y1:y1+y2,x1:x1+x2]
        template=src
        cv2.imwrite('template.jpg',template)


    #img = cv2.imread('1.jpg',0)
    img=gray.copy()
    
    
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
        print("相似度:{}".format(score),score)
        #cv2.imshow('roi',roi)
        if score >0.7:
            #设定相似度最低值
            cv2.rectangle(img,top_left, bottom_right, 255, 2)
            #如果相似画出框来

        cv2.imshow('hello',img)
cv2.destroyAllWindows()
