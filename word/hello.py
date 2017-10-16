from barcode.writer import ImageWriter
from barcode.codex import EAN13
from PIL import Image, ImageDraw, ImageFont, ImageWin
from io import StringIO

def generagteBarCode(self):
        imagewriter = ImageWriter()
        #保存到图片中
        # add_checksum : Boolean   Add the checksum to code or not (default: True)
        ean = Code39("1234567890", writer=imagewriter, add_checksum=False)
        # 不需要写后缀，ImageWriter初始化方法中默认self.format = 'PNG'
        #print '保存到image2.png'
        ean.save('image2')
        img = Image.open('image2.png')
        #print '展示image2.png'
        img.show()

        # 写入stringio流中
        #i = str(StringIO())
        global i
        ean = Code39("0987654321", writer=imagewriter, add_checksum=False)
        ean.write(i)
        i = StringIO(i.getvalue())
        img1 = Image.open(i)
        #print '保存到stringIO中并以图片方式打开'
        img1.show()
generagteBarCode(123)
