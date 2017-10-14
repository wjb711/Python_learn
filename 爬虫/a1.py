import urllib3,re
#导入模块，urllib3是上网，网页模块，re是正则表达式模块
urllib3.disable_warnings()
#去掉那些乱七八咋的warning

http = urllib3.PoolManager()
#建立连接池
headers = { #伪装为浏览器抓取    
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',  
    #'Accept-Language':'zh-CN',  
    'Content-type':'text/html;charset=utf-8'  
}
#伪装浏览器头部，现在很多网站都使用https协议，不伪装过不去。
url='http://ip138.com/'
#网站地址
r = http.request('GET', url,headers = headers)
try:
    content=r.data.decode('UTF-8')
except:
    content=r.data.decode('gb2312')

