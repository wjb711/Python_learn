import weixin_main,time,datetime,qiushi
from weixin_main import webpage1
from selenium.webdriver.common.keys import Keys
def test():
    print ('here112')
    print (webpage1.driver)
    print (weixin_main.driver)
    print ('end')
    #weixin_main.driver.find_element_by_class_name("main_inner")
    print ('here1')
    #print (weixin_main.driver.find_element_by_class_name("heroCanvas").is_displayed())      
def test2():
    print ('nothing')
    print ('12sdfas3')
    elem = a1.driver.find_element_by_id("editArea")

    print ('12sdfas31112')
        #要输入的文本内容

    b=str(datetime.datetime.now())
    b=qiushi.main1()

    print (b)
    elem.send_keys(b)
    print ('1')
    time.sleep(2000)
    elem.send_keys(Keys.ENTER)
    print ('2')
   
