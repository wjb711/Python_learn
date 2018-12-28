import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from fpdf import FPDF
import random
import datetime
import os
day0=input('请输入要生成报告的日期:')
x=datetime.datetime.strptime(day0, '%Y%m%d')
x0=str(x.strftime('%Y.%m.%d'))
y = x - datetime.timedelta(days=7)
y0=str(y.strftime('%Y.%m.%d'))
print (x0)
print (y0)

#设置所使用的字体
font = ImageFont.truetype("shouxie.ttf", 28)

#打开图片
imageFile = "1.jpg"
im1 = Image.open(imageFile)

#画图
draw = ImageDraw.Draw(im1)


l1=int(random.uniform(325,370))

w1=str(int(random.uniform(20,25)))
draw.text((l1, 140), w1, (70, 65, 68), font=font)

l2=int(random.uniform(325,370))
w2=str(int(random.uniform(38,51)))
draw.text((l2, 170), w2, (70, 65, 68), font=font)

l1=int(random.uniform(325,370))
w1=str(int(random.uniform(20,25)))
draw.text((l1, 405), w1, (70, 65, 68), font=font)

l2=int(random.uniform(325,370))
w2=str(int(random.uniform(38,51)))
draw.text((l2, 440), w2, (70, 65, 68), font=font)


t=int(random.uniform(20,40))
l2=int(random.uniform(150,350))
font1 = ImageFont.truetype("shouxie.ttf", t)
draw.text((900, l2), "周XX", (70, 65, 68), font=font1)    #设置文字位置/内容/颜色/字体

t=int(random.uniform(20,40))
l2=int(random.uniform(150,350))
font1 = ImageFont.truetype("shouxie.ttf", t)
draw.text((1000, l2), "王XX", (70, 65, 68), font=font1)    #设置文字位置/内容/颜色/字体

t=int(random.uniform(20,40))
l2=int(random.uniform(150,350))
font1 = ImageFont.truetype("shouxie.ttf", t)
draw.text((1080, l2), y0, (70, 65, 68), font=font1)    #设置文字位置/内容/颜色/字体

t=int(random.uniform(20,40))
l2=int(random.uniform(420,650))
font1 = ImageFont.truetype("shouxie.ttf", t)
draw.text((900, l2), "沈X", (70, 65, 68), font=font1)

t=int(random.uniform(20,40))
l2=int(random.uniform(420,650))
font1 = ImageFont.truetype("shouxie.ttf", t)
draw.text((1000, l2), "周XX", (70, 65, 68), font=font1)


t=int(random.uniform(20,40))
l2=int(random.uniform(420,650))
font1 = ImageFont.truetype("shouxie.ttf", t)
draw.text((1080, l2), x0, (70, 65, 68), font=font1) 

draw = ImageDraw.Draw(im1)                          #Just draw it!

#另存图片
#im1.save("target.jpg")
try:
    os.mkdir('report')
except:
    pass
im1.save('./report/'+day0+'.pdf', "PDF" ,resolution=200.0, save_all=True)
os.system('./report/'+day0+'.pdf')
