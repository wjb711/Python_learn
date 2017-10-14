import urllib3,re
urllib3.disable_warnings()  

http = urllib3.PoolManager()
headers = { #伪装为浏览器抓取    
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',  
    #'Accept-Language':'zh-CN',  
    'Content-type':'text/html;charset=utf-8'  
} 
r = http.request('GET', 'http://ip.cn/',headers = headers)
content=r.data.decode('UTF-8')
print (content)
pattern = re.compile('<code>(.*)</code>',re.S)
items = re.findall(pattern,content)
print ('***************************************************')
print (items)
