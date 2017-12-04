import wget
import json
import jsonpath

#url = 'http://www.sojson.com/open/api/weather/json.shtml?city=%E5%8C%85%E5%A4%B4'
url='https://news.baidu.com'
#url链接，网上找的测试用
filename = wget.download(url)
#定义下载用的名称
#print (filename)
input=open(filename,'r',encoding = 'utf-8')
#打开此文件，注意用utf-8解码
jsonobj=json.load(input)
#print (jsonobj)
#使用json.load加载
citylist = jsonpath.jsonpath(jsonobj,'$..head')
print (citylist)
#jsonpath提取城市名
#D = jsonpath.jsonpath(jsonobj,'$..id')
#jsonpath提取ID
#rint (len(citylist),type(citylist),citylist[0])
#or i in range(len(citylist)):
 #   print (ID[i],citylist[i])
