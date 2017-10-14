import cv2
cap=cv2.VideoCapture(1)
ret=cap.set(3,5000)
ret=cap.set(4,5000)
ret=cap.set(15,-1)
#cap.set(10,230)#亮度，最高250
#cap.set(11,200)#对比度，最高250


n=0
time=10

dict={}

while 1:
    #print (cap.get(3))
    #print (cap.get(4))
    #print (cap.get(14))
    #print (cap.get(15))
    _,frame=cap.read()
    #d=d+frame
    cv2.imshow('1',frame)
    #cv2.imshow('d',d)
    cv2.waitKey(1)
    dict[n]=frame
    
    f=0
    y=time
    if n>y:
        del dict[n-y-1]
        #print ('n is ',n)
        while y>=1:
            #print ('y is ',y)
            y=y-1
            f=cv2.add(f,dict[n-y])
            
            
        cv2.imshow('f',f)
        
        #e=dict[n]+dict[n-1]+dict[n-2]+dict[n-3]+dict[n-4]+dict[n-5]
        
        
        
    n=n+1
    
