import cv2
import datetime,time
import unittest,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class PythonOrgSearch(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
 
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://t.cn/R9U4xwG")
        #self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("editor")
        #要输入的文本内容
        #elem.send_keys("印度儿童纪录片")
        #time.sleep(5)
        #elem.clear()
        #elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source
        ele=driver.find_element_by_tag_name("input")
        #<i class="icon-pic iconfont icon-mailbox_icon_addpic_1"></i>
        time.sleep(2)
        #ele.click()
        print ("done")
        #图片位置，必须是绝对路径
        ele.send_keys("C:\\CV\\Github\\Opencv_learning\\face\\pic.jpg")
        time.sleep(5)
        driver.find_element_by_id("btnPreview").click()
 
    def tearDown(self):
        print ('done1')
        #self.driver.close()
        print ('done2')
        #pass
def miaomiao():
    driver.get("http://t.cn/R9U4xwG")
        #self.assertIn("Python", driver.title)
    elem = driver.find_element_by_name("editor")
    elem.send_keys("印度儿童纪录片")
        #time.sleep(5)
        #elem.clear()
        #elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source
    ele=driver.find_element_by_tag_name("input")
        #<i class="icon-pic iconfont icon-mailbox_icon_addpic_1"></i>
    time.sleep(2)
        #ele.click()
    print ("done")
    ele.send_keys("C:\\CV\\Github\\Opencv_learning\\face\\pic.jpg")
    time.sleep(3)
    driver.find_element_by_id("btnPreview").click()
    time.sleep(15)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
cap=cv2.VideoCapture(0)
driver = webdriver.Chrome()
while 1>0:
    _,image=cap.read()
    #image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    print (faces)
    if faces is ():
        print ('no face')
    else:
        for (x,y,w,h) in faces:
            #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            ball = image[y:480, x:640]
            #cv2.imshow('ball',ball)
            #
            cv2.imwrite('pic.jpg',ball)
            time.sleep(2)
            #input("hello:")
            miaomiao()
        print ('yes')
    cv2.imshow('hello',image)
    cv2.waitKey(10)
