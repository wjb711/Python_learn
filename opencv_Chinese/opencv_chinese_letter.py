import cv2,numpy
#导入cv2,numpy模块
from PIL import Image,ImageDraw,ImageFont
#导入PIL模块下的图片，绘图，字体模块
cap=cv2.VideoCapture(0)
while True:
#    _,frame=cap.read()
    _,frame = cap.read()
    #cv2_im = cv2.cvtColor(cv2_im,cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    #转化opencv图片格式为PIL格式
    #img=Image.open(pic)
    imgSize=img.size
    font = ImageFont.truetype('simhei.ttf', int((imgSize[0])*0.04))
    #设定字体，和字符大小
    draw = ImageDraw.Draw(img)
    #draw.text(((imgSize[0]-320), (imgSize[1]*0.96)), '捷德中国.影音协会', (255,0,0), font=font)，注意格式是蓝绿红BGR
    draw.text((imgSize[0]*0.6, (imgSize[1]*0.9)), '捷德中国.影音协会', (0,0,255), font=font)
    #再次转换PIL格式，回到opencv格式
    open_cv_image = numpy.array(img)
    #pil_im.show()
    #tmp=frame.copy()
    #img = Image.fromstring('L', (480,640), frame, 'raw', 'F;16')
    #print (frame.size)
    #im.load(tmp)
    #draw = ImageDraw.Draw(pil_im)
    cv2.imshow('frame',open_cv_image)
    if cv2.waitKey(1)==ord('q'):
        print ('quit')
        break
cap.release()
cv2.destroyAllWindows()
