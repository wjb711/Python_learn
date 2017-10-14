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
url='http://1212.ip138.com/ic.asp'
#网站地址,ip138其实调用了一个asp子网页，这个是从网页源代码看出来的
#那么就简单了，咱们针对这个asp网页做爬虫抓取。
r = http.request('GET', url,headers = headers)
#请求一个网页
try:
    content=r.data.decode('UTF-8')
except:
    content=r.data.decode('gb2312')

#中文转码
pattern = re.compile('<center>(.*?)</center>',re.S)

b=re.findall(pattern,content)
#正则表达式，查询的内容，注意问号为最小查询，否则返回最大查询
print (b[0])
#打印我们要的内容。
