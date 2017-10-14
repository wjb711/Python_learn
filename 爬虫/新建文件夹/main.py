import time,imp,a2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#driver=''
global driver
driver = webdriver.Chrome()
driver.get("https://wx.qq.com/")
b=a1.driver.find_element_by_class_name("login_box").is_displayed()

def try1():
    try:
        print ('try')
        imp.reload(a2)
        print ('reload done')
        a2.test()
        print ('a2 test done')
    except:
        print ('except')
        imp.reload(a2)
        time.sleep(3)
        try1()
while True:
    #imp.reload(a2)
    try1()
    print ('done')
    
    time.sleep(3)
