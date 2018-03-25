import tkinter,cv2,PIL,numpy
from PIL import Image,ImageDraw,ImageFont,ImageGrab
from aip import AipOcr
import easygui
import os

def mouse_action(event,x,y,flags,param):
    imageText = img.copy()
    cv2.putText(imageText, str(x)+'+'+str(y), (200, 200), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 0 ,0), thickness = 4, lineType = 8)
    cv2.imshow("window_full", imageText)
    global img_copy
    #self.mouse_break=0
    #global mode,x0,y0,x1,y1,mouse_break
    print (event,x,y,flags,param)

            
    #点击按钮后，截屏，并全屏显示    
def button_command():
    #a.mode=0
    #a.mouse=False
    print ('start here')
    
    global img,img_copy,x,y
    #filename = 'temp.png'
    im = ImageGrab.grab()
    #im.show()
    #im.save(filename)
    #im.close()
    #im=pyautogui.screenshot()
    imgSize=im.size
    font = ImageFont.truetype('simhei.ttf', int((imgSize[0])*0.025))
    draw = PIL.ImageDraw.Draw(im)
    draw.text((imgSize[0]*0.7, (imgSize[1]*0.92)), '拖拽鼠标截图，取消按ESC', (255,0,0), font=font)
    
    img=numpy.array(im)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_copy=img.copy()
        #img =  cv2.imread('1.png')
    cv2.namedWindow("window_full", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window_full",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    
    cv2.setMouseCallback('window_full',mouse_action)
    print ('mid here')
    cv2.imshow("window_full", img)
    #global imageText
    while True:
        pass
        #imageText = img.copy()  
        
        #cv2.imshow("window_full", imageText)

        #print ('mouse_break',self.mouse_break)
    #    print ('loop here')
        if cv2.waitKey(1)==27:
            print ('esc pressed')
            break
    #    else:
    #        print (x,y)
    #        print ('self.mode,')

    cv2.destroyWindow("window_full")
    

    #鼠标操作，先按下移动，画出矩形框

button_command()
