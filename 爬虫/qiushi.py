import urllib3,re,time
#导入模块，urllib3是上网，网页模块，re是正则表达式模块

import multiprocessing.pool
import functools
#下面这两个，是为了引入timeout这个参数


#timeout这个是抄过来的，没有细研究
def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator


@timeout(2.5)
def downloadwebpage(url):
    #url='https://www.qiushibaike.com'
    #网站地址
    print ('3')
    print (url)
    print (headers)
    r = http.request('GET', url,headers = headers)
    print (r)
    print ('4')
    #请求一个网页
    print ('page download success')
    try:
        content=r.data.decode('UTF-8')
    except:
        content=r.data.decode('gb2312')

    #中文转码
    print ('page decode success')
    return content
#防止网页超时，超时自动再来一次
def try_1():
    try:
        global content
        content=downloadwebpage(url)
        print ('content done')
        #print ('m1 is',myword)
    except Exception as err:
        print ('download error')
        time.sleep(10)
        #print ('Exception',Exception)
        try_1()
def main1():
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
    global url
    url='https://www.qiushibaike.com'
    print ('1')
    
    try_1()
    print ('2')
    #content=downloadwebpage(url)
    pattern = re.compile('<span>(.*?)</span>',re.S)

    b=re.findall(pattern,content)
    #正则表达式，查询的内容，注意问号为最小查询，否则返回最大查询
    print ('你的IP是'+b[0],'\n你的地址是'+b[1])
    #打印我们要的内容。
    return b[0]
    

if __name__=='__main__':
    main1()
    
