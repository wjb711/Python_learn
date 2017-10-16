from barcode.writer import ImageWriter
from barcode.codex import Code13
from PIL import Image, ImageDraw, ImageFont, ImageWin
from io import StringIO
#import cv2

def generagteBarCode(x,y):
        imagewriter = ImageWriter()
        #保存到图片中
        # add_checksum : Boolean   Add the checksum to code or not (default: True)
        ean = Code13(x, writer=imagewriter, add_checksum=False)
        # 不需要写后缀，ImageWriter初始化方法中默认self.format = 'PNG'
        print ('保存到image2.png')
        #cv2.imshow('ean',ean)
        ean.save('./barcode/'+x)
        #draw.text((imgSize[0]*0.6, (imgSize[1]*0.9)), '捷德中国.影音协会', (255,0,0), font=font)
        img = Image.open('./barcode/'+x+'.png')
        print (x+'.png')
        
        
        imgSize=img.size
        font = ImageFont.truetype('simhei.ttf', int((imgSize[0])*0.04))
        #设定字体，和字符大小
        draw = ImageDraw.Draw(img)
        #draw.text(((imgSize[0]-320), (imgSize[1]*0.96)), '捷德中国.影音协会', (255,0,0), font=font)
        draw.text((imgSize[0]*0.05, (imgSize[1]*0.75)), y, (0,0,0), font=font)
        #设定字开始的位置，字的内容，颜色等等
        img.save('./barcode/'+x+'.png', 'PNG')

        img.show()

generagteBarCode('hello31a456','你好1呀')
