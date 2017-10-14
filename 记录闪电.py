import cv2,datetime
'''
简单说下原理，截取摄像头的每一帧图， 计算光亮部分的面积， 如果超出前一张图的几倍（可自定义），则抓取并保存当前图片
也就是说，当闪电时，比前面要亮好多，那么保存图像
'''
def max_cap_size():
    cap.set(3,3000)
    cap.set(4,3000)
    return(int(cap.get(3)),int(cap.get(4)))
def cap_para():
    cap.set(10,250)#亮度，最高250
    cap.set(11,250)#对比度，最高250
    cap.set(15 ,2)#曝光时间，最高0，普通-4
cap=cv2.VideoCapture(0)
max_cap_size()
cap_para()
#打开摄像头
last=1
#给上一张图初始化赋值
while True:
#while循环开始
    _,frame=cap.read()
    #读取frame帧
    gray=cv2.cvtColor(frame,6)
    #转化为灰度图

    _,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    #二值化，或阀值化，其中“200”需要根据白天，晚上等具体调节，白天高一点，晚上低一点如120
    _,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #统计白色部分的轮廓
    sum=0
    for cnt in contours:
        sum=sum+cv2.contourArea(cnt)
    #计算亮白色闪电部分的总面积
    try:
        print (sum/last)
        if sum/last >3:
        #如果当前总面积比上一张图的总面积大三倍
            now = datetime.datetime.now()
            #取日期，保存图片时使用
            #print ("yes")
            im_name1=(now.strftime('%Y-%m-%d_%H%M%S')+'.jpg')
            #图片名称
            cv2.imwrite(im_name1,frame)
            #写入当前的闪电照片
            #cv2.imshow('Photo',im_all)
            cv2.imwrite('1.png',frame)
            print ('done')
    except:
        #如果不够亮，pass
        pass
    
    last=sum
    #print (sum)
    cv2.imshow('1',frame)
    #显示摄像头的图
    cv2.imshow('2',thresh)
    #显示阀值图
    #print (thresh.size)
    
    cv2.waitKey(30)
    #时间间隔，30毫秒
