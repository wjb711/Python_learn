import weixin_main,time,datetime,糗事百科抓文字
from selenium.webdriver.common.keys import Keys
def timer():
    print ('hello011')
    #间隔时间
    timedelta=datetime.timedelta(minutes=1)
    #取当下时间
    now = str(datetime.datetime.now())[:-7]
    next=now
    #判断是否开始时间已错过,如果结果为负数，则提示错误

    while True:
        print ('hello012')
        now = str(datetime.datetime.now())[:-7]
        if now==next:
            #print (sched_time)
            next=str(datetime.datetime.now()+timedelta)[:-7]
            #print (sched_time)
            print ('请在这里开始你的程序')
            chat=糗事百科抓文字.main()
            print ('abc is ',chat)
            test(name,chat)
        time.sleep(1)
        print (now)
def test(name,chat):
    print ('hello011')
    #间隔时间
    timedelta=datetime.timedelta(minutes=5)
    #取当下时间
    now = str(datetime.datetime.now())[:-7]
    next=now
    #判断是否开始时间已错过,如果结果为负数，则提示错误

    while True:
        print ('hello012')
        now = str(datetime.datetime.now())[:-7]
        if now==next:
            #print (sched_time)
            next=str(datetime.datetime.now()+timedelta)[:-7]
            #print (sched_time)
            print ('请在这里开始你的程序')
            chat=糗事百科抓文字.main()
            print ('abc is ',chat)
                #elem = weixin_main.driver.find_element_by_name("editor")
            #elem = weixin_main.driver.find_element_by_class_name("web_wechat_search")
            friend_name = weixin_main.driver.find_element_by_tag_name("input")
            #elem.click()
            friend_name.send_keys(name)
            time.sleep(3)
            friend_name.send_keys(Keys.ENTER)
            chat_content = weixin_main.driver.find_element_by_id("editArea")
            time.sleep(1)
            chat_content.send_keys(chat)
            time.sleep(2)
        time.sleep(1)
    #chat_content.send_keys(Keys.ENTER)
    #elem.send_keys(Keys.ENTER)
    print ('ok here1')
    
    print ('ok here')

