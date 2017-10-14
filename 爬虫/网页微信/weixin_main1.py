import time,imp
#time时间工具，imp重新加载模块工具，weixin_action,微信内部动作模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://wx.qq.com/")
    #selenium以及chrome模块
    #webpage1()
    login()
    #weixin_action的循环时间
    time1=5
    while True:
        time.sleep(time1)
        try1()
        
    print ('main done')

def login():
    while driver.find_element_by_class_name("login_box").is_displayed():
        time.sleep(3)
        print ("请拿起手机扫码登录")
    print ('login done')
def try1():
    global name
    global chat
    name="燕子"
    chat="你好"
    try:
        print ('try',driver)
        imp.reload(weixin_action)
        print ('reload done')
        weixin_action.test(name,chat)
        print ('a2 test done')
    except:
        print ('except')
        imp.reload(weixin_action)
        time.sleep(3)
        try1()
    print ('try1 done')
        


