import cv2
import numpy as np
import easygui as g
g.msgbox('图片叠加比对程序，纯手动键盘操作， 上（w）下(s)左(a)右(d),放大（m）,缩小（n）')
file0=g.fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
print(file0)
file1=g.fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
print(file1)
img0=cv2.imread(file0)

rows0=img0.shape[0]
cols0=img0.shape[1]
rate0=cols0/rows0
print(rows0,cols0)
rows_init=400
rows0=int(rows_init)
cols0=int(rows0*rate0)
img0=cv2.resize(img0,(cols0,rows0),0,0)


img1=cv2.imread(file1)

rows1=img1.shape[0]
cols1=img1.shape[1]
rate1=cols1/rows1
print(rows1,cols1)
rows1=int(rows_init)
cols1=int(rows1*rate1)
img1=cv2.resize(img1,(cols1,rows1),0,0)



k=0
x0=150
x1=x0
y0=100
y1=y0
cv2.namedWindow('pic', 0)
while k!=27:
    k=cv2.waitKey(1)
    if k==109:
        rows0=int(rows0*1.01)
        cols0=int(rows0*rate0)
        
        #cv2.imshow('dst0',dst0)
    if k==110:
        rows0=int(rows0*0.99)
        cols0=int(rows0*rate0)
        
        #cv2.imshow('dst0',dst0)        
        
    elif k==115:
        y0=y0+1
    elif k==119:
        y0=y0-1
    elif k==97:
        x0=x0-1
    elif k==100:
        x0=x0+1
    elif k==-1:
        pass
    else:
        print(k)
    #cv2.imshow('img0',img0)
    dst0=cv2.resize(img0,(cols0,rows0),0,0)
    #cv2.imshow('dst0',dst0)
    rows_max=max(y1+rows1,y0+rows0)
    cols_max=max(x1+cols1,x0+cols0)
    pic0=np.zeros((rows_max,cols_max,3),np.uint8)
    pic1=pic0.copy()
    pic0[y0:y0+rows0,x0:x0+cols0]=dst0
    
    pic1[y1:y1+rows1,x1:x1+cols1]=img1
    pic = cv2.addWeighted(pic0,0.5,pic1,0.5,0) 
    #cv2.imshow('pic0',pic0)
    #cv2.imshow('pic1',pic1)
    cv2.imshow('pic',pic)
cv2.destroyAllWindows()
    
