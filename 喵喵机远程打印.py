import unittest,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
"""
大家知道，喵喵机是手机通过蓝牙连接的
官方说，目前不支持其他方式
真的吗？
对于一个喜欢diy的人，这些都不是个事。
首先手机喵喵机的客户端上，打开我的信箱，选择永久， 纸条选择立即打印， 然后

选择发送到微信朋友
当然是发给《微信传输助手》，然后通过这个， 我们在浏览器打开，就可以获得一

个永久的网页链接
温馨提示， 手机上还要设着喵喵机的免杀， 免得黑屏后被系统进程杀掉。
这个名字有点长， 需要改短一点，上网搜新浪短网址， 就可以缩短到很短，例如
这时，，把这个分享给远方的她/他， 就可以远程使用啦，当然电脑上也可以打开。


下面是python的脚本， 可以插入要写得字，还有图片
服了贴吧，总说违规，自己到github上搜索。
"""
 
class PythonOrgSearch(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
 
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://t.cn/R9U4xwG")
        #self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("editor")
        #要输入的文本内容
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
        #图片位置，必须是绝对路径
        ele.send_keys("C:\\CV\\Github\\Opencv_learning\\pic.jpg")
        time.sleep(15)
        driver.find_element_by_id("btnPreview").click()
 
    def tearDown(self):
        #self.driver.close()
        pass
 
if __name__ == "__main__":
    unittest.main()
