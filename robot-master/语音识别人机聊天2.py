# 引入Speech SDK
from aip import AipSpeech
#import json
import recorder
import os,sys,time
#import turing
import urllib.request
import win32com.client
from urllib.parse import quote
#下面这两个，是为了引入timeout这个参数
import multiprocessing.pool
import functools

#myword='hello'
def start():#这个是开场白
#speaker = win32com.client.Dispatch("SAPI.SpVoice")
#print ('hello01')
    print ("我是捷德中国智能机器人图灵大白，想聊点什么？\n")

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
#录音，用百度语音识别，并图灵回答问题
def recorder_ok():
    #录音，超过两秒，小于10秒即可，超出范围，直接pass
    isOk=recorder.recorder()
    if isOk:
        #print (isOk)
        #print ('recording finish')
        #x=time.time()
        try_1()
        #y=time.time()
        #print ('time is ',y-x)
        if myword !="听不清":
            tuling()
        
    else:
        print ('pass')
def try_1():
    try:
        baiduyuyin()
        #print ('m1 is',myword)
    except Exception as err:
        #print ('Exception',Exception)
        try_1()
    
def tuling():
    #print (myword)
    dic={'你的爸爸': "王剑波",
             '捷德中国': "捷德集团是一家总部设在德国慕尼黑的国际领先技术供应商。公司成立于1852年，已经成功经营了160多年。捷德在全球拥有超过一万一千名员工，2012财年的销售额达到17.94亿欧元。为了更好地服务客户，捷德公司在全球32个国家已建立了58家子公司和合资企业",
             '你爸爸是谁':"王剑波,一枚大帅哥",
             '你爸爸':"王剑波,一枚大帅哥",
             #'我是谁':"王靖萱呀",
             '你的爸爸是谁':"王剑波,一枚大帅哥",
             '你的爸爸是谁呀':"王剑波,一枚大帅哥",
             '王静轩':"王靖萱，小美女一枚,当红大歌星",
             '王俊轩':"王靖萱，小美女一枚，当红大歌星",
             '陈燕':"王靖萱的妈妈，王剑波的老婆",
             '王剑波':"王靖萱的爸爸，陈燕的老公",
             '王建波':"王剑波，王靖萱的爸爸，陈燕的老公",
             '王俊仙':"王靖萱，小美女一枚",
             }
        #自定义的问题库

            
        #myword=keywords[0][:-1]
    print ("我："+myword)
        #print (type(myword))
    if myword in dic:
        feedback=dic[myword]
        print ('in')
        #如果在问题库里有，就显示问题库里的答案
        #如果没有就上网上搜取图灵机的答案
    else:
            #输入提示符
            #myword='你会说话不'
        #url0='http://www.tuling123.com/openapi/api?key=29ccde937cd544afbd45667b4be9805e&userid=12345&info='+myword
        url0='http://www.tuling123.com/openapi/api?key=4db21f83439a494091bdcde7e8f01770&userid=12345&info='+myword
            #图灵的网址+自己创建的myword关键词
        url=('\n%s' % quote(url0, safe='/:&?='))
            #把中文关键词转化为url能够接受的形式
            #print (url)
            #如果没有网络，或其他错误，显示没有网络
        try:
                
            fb=urllib.request.urlopen(url)
            mybytes=fb.read()
            mystr=mybytes.decode('utf8')
            feedback=eval(mystr)['text'].replace("曾先森", "捷德中国").replace("曾庆涛", "王剑波")
            #feedback=eval(feedback)['text'].replace("曾庆涛", "王剑波")
                #替换，把曾先森换为捷德中国
        except:
            feedback="没有网络，不跟你好啦"
        #print (feedback.replace("曾先森", "捷德"))
    print ("大白："+feedback)
        #print (type(feedback))
        
    speaker.Speak(feedback)
            #说出话来
@timeout(2.5)
def baiduyuyin():
    global myword
    APP_ID = '9424816'
        #print ('hello03')
    API_KEY = 'qaCMG6wQ0WVejR1IpXoS1ABB'
    #print ('hello04')
    SECRET_KEY = '4c36038b7b31ab119b9a56ed88f70229'
    #print ('hello05')
    # 初始化AipSpeech对象
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    #print ('hello06')

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
    #        print ('hello07')
    #        print (fp)
            return fp.read()
    # 识别本地文件
    #print ('hello08')
    #os.system('output.wav')
    try:
        #print ('hellllll')
        #print ('start here')
        result = aipSpeech.asr(get_file_content('output.wav'), 'wav', 8000, {'lan': 'zh'})
        #print (result)
        keywords=result['result']
        myword=keywords[0][:-1]
    except Exception as err:
        #print ("听不清,杂音")
        myword="听不清"
    #print ('myword is ',myword)
    return myword
        
    

if __name__=='__main__':
    #print ('start here')
    global speaker
    global myword
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    start() #开场白
    while True:
        recorder_ok()
    
    
    
    
