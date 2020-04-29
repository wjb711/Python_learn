#需求来自需要复制网站的一个子目录做备份用途， 网上的工具要么没图片， 要么没附件，要么特别的慢
#所以我们结合wget的网页下载功能，完成网站内容的备份
#首先我们要备份的链接是保存在一个CSV文件中的
#大致格式如下
'''
链接            部门          网页标题
http://www.baidu.com/28D0A6C9EF273004E0530A0404E63004	运营	精益生产在中国的一年
http://www.baidu.com/A2CF3173A9BBB082E0430A0404E6B082	采购	战略采购部
http://www.baidu.com/A2CF772D4F76A0FAE0430A0404E6A0FA	采购	供应链管理部.
http://www.baidu.com/A2CF772D4F76A0FAE0430A0404E6A0FA	采购	供应链管理部.
'''
from bs4 import BeautifulSoup#用于解析网页
import urllib3

import csv
import os

http =urllib3.PoolManager()

#首先读取csv文件，key是链接有唯一性， 值是包含部门和标题的列表
dict0={}
with open('Book3.csv', 'r') as f:
    reader = f.readlines()
    #print(type(reader))
    for row in reader:
        list0=row.split(',')
        dict0[list0[0]]=[list0[1],list0[2]]


#依据字典列表（链接表），逐个执行下载
for x in dict0:
    print(x,dict0[x])
    name0=(x.split('/')[6])
    name1=dict0[x][0]+'-'+dict0[x][1]+'.html'
    #wget此网页 包含jpg 拒绝下载png, gif js等
    cmdx='wget --convert-link -p -np -k -R  --reject=png  --reject=js  --reject=gif --reject=css '
    cmd=cmdx+x
    print(cmd)
    os.system(cmd)
    print('download end*************************************************************')
    #有时候网页包含的下载链接并不在本页中， 而是新的一个链接， 这样我们就做外链的扩展扫描， 当然这样非常慢， 时间指数级增加
    #如果下载的内容都在本页， 可以把下面全部注释掉
    try:
        #打开当前下载好的网页，并读取所有的链接
        with open('abc.baidu.com/portal/page/portal/'+name0,'r') as f:
            html=str(f.readlines())
        bsObj = BeautifulSoup(html, 'html.parser')
        t1 = bsObj.find_all('a')
        for t2 in t1:
            try:
                #尝试读取链接的头文件， 根据头文件是text或application做不同的处理
                t3 = t2.get('href')
                print(t3)
                r=http.request('GET',t3)
                print(r.headers['content-type'])
                headers0=r.headers['content-type']
                print(headers0, type(headers0),headers0[:4])
                if headers0[:4]=='text':
                    print('text',t3)
                    link0=t3
                    cmd=cmdx+link0
                    print('text_html to download',t3)
                    os.system(cmd)

                else:
                    link0=t3
                    cmd=cmdx+link0
                    print('file to download',t3)
                    os.system(cmd)
            except:
                pass
        #最后把下载好的网页另存为部门名称+网页标题的格式， 完成
        os.rename('eplanet.gi-de.com/portal/page/portal/'+name0,'eplanet.gi-de.com/portal/page/portal/'+name1)
    except:
        print('error')
#        a=input(dict0[x][0]+':'+dict0[x][1])
#    a=input(dict0[x][0]+':'+dict0[x][1])
