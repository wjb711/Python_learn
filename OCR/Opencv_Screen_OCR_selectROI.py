#本程序目的是截取屏幕，上传至数据库， ocr识别文字后发回客户端
#依赖库的安装pip install opencv-python Pillow baidu-aip easygui
#大致方法是，1，tkinter创建窗口，上面有一个按钮button, 按钮位于屏幕右下角
#按下按钮后， 截屏，并满屏显示，再后来使用opencv截取矩形框，也就是需要识别文字的地方
#最后，把图片上传到服务器上，获取到在线ocr文字后，同过easygui返回。
import tkinter,cv2,PIL,numpy
from PIL import Image,ImageDraw,ImageFont,ImageGrab
from aip import AipOcr
import easygui
import os
   



class OCR():
    #mode=0
    #mouse=False
    
    def __init__(self):
        self.window()

    #创建窗口   
    def window(self):
        window=tkinter.Tk()
        #window.title('转文本')
        position_x=window.winfo_screenwidth()-150
        window.geometry('%dx%d+%d+%d' % (100,30,(window.winfo_screenwidth()-100), (window.winfo_screenheight() - 100) ))
        window.resizable(width=False, height=False)

        button0=tkinter.Button(window, text="截图转文字", command=self.button_command).pack()
        window.mainloop()


    #点击按钮后，截屏，并全屏显示    
    def button_command(self):
        self.mode=0
        self.mouse=False
        print ('start here')
        
        global img,img_copy
        #filename = 'temp.png'
        im = ImageGrab.grab()
        #im.save(filename)
        #im.close()
        #im=pyautogui.screenshot()
        imgSize=im.size
        font = ImageFont.truetype('simhei.ttf', int((imgSize[0])*0.025))
        draw = PIL.ImageDraw.Draw(im)
        draw.text((imgSize[0]*0.7, (imgSize[1]*0.92)), '拖拽鼠标截图，敲回车键继续', (255,0,0), font=font)
        
        img=numpy.array(im)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img_copy=img.copy()
            #img =  cv2.imread('1.png')
        cv2.namedWindow("ROI selector", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("ROI selector",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        r = cv2.selectROI(img_copy)
        imCrop = img_copy[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        #cv2.imshow('new',imCrop)
        cv2.destroyAllWindows()
        #cv2.setMouseCallback('window_full',self.mouse_action)
        print ('mid here')
        cv2.imwrite('t.png',imCrop)
        self.baidu_ocr()
     
    def baidu_ocr(self):
        print ('start')
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
        easygui.msgbox(sum0,title='截图转文字（可复制）：捷德IT部出品')
        os.remove('t.png')



if __name__=='__main__':
#内网代理的配置与使用
    #os.environ['https_proxy']='http://wanjianb:Beijing123_@web-gate4a.accounts.intern:3128'
    OCR()

