import urllib3,re,os,requests
from tqdm import tqdm
#导入模块，urllib3是上网，网页模块，re是正则表达式模块
#注意需要下载wget.exe到同级文件夹，pdf最终通过wget.exe来下载

import multiprocessing.pool
import functools


def downloadwebpage(url):
    
    #url='https://www.qiushibaike.com'
    #网站地址
    #input('anykey to continue0:')
    r = http.request('GET', url,headers = headers)
    #input('anykey to continue1:')
    #请求一个网页
    #print ('page download success')
    try:
        content=r.data.decode('UTF-8')
    except:
        #content=r.data.decode('gb2312')
        content=''

    #中文转码
    #print ('page decode success')
    return content

def openpage(url):
    #print ('start')
    urllib3.disable_warnings()
    #去掉那些乱七八咋的warning
    global http
    http = urllib3.PoolManager()
    #建立连接池
    global headers
    headers = { #伪装为浏览器抓取    
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',  
    #'Accept-Language':'zh-CN',  
    'Content-type':'text/html;charset=utf-8'  
    }
    #伪装浏览器头部，现在很多网站都使用https协议，不伪装过不去。
    #global url
    #url='https://www.etsi.org/deliver/'
    #url='https://www.etsi.org/deliver/etsi_en/300001_300099/'
    #url='https://www.etsi.org/deliver/etsi_en/300001_300099/300001/01.05.01_60/'
    
    
    #print ('url is ',url)
    #try_1()
    content=downloadwebpage(url)
    #print (content)
    #print ("******************",'\n')
    image_list = content.strip(',').split('HREF="')
    for x in image_list:
        if "Parent" in x:
            pass
        else:
            x1=x.split('"')[0]
            if "html" in x1:
                pass
            elif '.pdf' in x1:
                print (webhead+x1,'\n')
                filename=x1.split('/')[-1]
                folder=x1[:-len(filename)]
                print (folder,filename)
                try:
                    os.makedirs('.'+folder)
                except:
                    print (folder)
                    print ('fail')
                    pass
                #判断文件是否下载过
                if os.path.exists("."+x1):
                    print ('文件已下载，跳过')
                    pass
                else:
                    #下载文件的具体步骤
                    try:
                        os.system("wget.exe "+webhead+x1+" -P "+'.'+folder)
                        #response = requests.get(webhead+x1, stream=True)
                        #with open("."+x1, "wb") as handle:
                        #    for data in tqdm(response.iter_content()):
                        #        handle.write(data)
                    except:
                        pass
                #downloadwebpage(webhead+x1)
                #os.makedirs(x1)
                #x2=x1.split('/')[-1]
                #f = open(x2, 'wb')
                #f.write((urllib.request.urlopen(webhead+x1)).read())
                #print(imgPath)
                #f.close()
            else:
                #print (x,'\n',"***",'\n',x1)
                #print (webhead+x1)
                
                openpage(webhead+x1)
    #pattern = re.compile('<span>(.*?)</span>',re.S)

    #b=re.findall(pattern,content)
    #正则表达式，查询的内容，注意问号为最小查询，否则返回最大查询
    #print ('讲个笑话'+b[0])
    #打印我们要的内容。
    #return(b[0])

if __name__=='__main__':
    webhead='https://www.etsi.org'
    url='https://www.etsi.org/deliver/etsi_en/'
    openpage(url)
