import weixin_main1,time
from selenium.webdriver.common.keys import Keys
from weixin_main1 import main1
def test(name,chat):
    print ('ok here')
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
    #elem.send_keys(Keys.ENTER)
    print ('ok here1')
