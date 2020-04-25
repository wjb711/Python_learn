import os
import time
import requests
#原理， 模拟浏览器向Kibana发出请求
#通过linux的curl post方法发出数据，下面链接的获取方法是通过chrome浏览器，F12, Network, copy as cURL(bash)
cmd=r"curl $'http://10.102.12.32:5601/api/reporting/generate/csv?jobParams=(conflictedTypesFields:\u21(),fields:\u21(%27@timestamp%27,fields.logtype,%27Source%20IP%27,EvenName,EventDetails,UserResponsible,Request-ID,Session-ID),indexPatternId:%2738c4b240-9b94-11e8-9f63-57876205648d%27,metaFields:\u21(_source,_id,_type,_index,_score),searchRequest:(body:(_source:(excludes:\u21(),includes:\u21(%27@timestamp%27,fields.logtype,%27Source%20IP%27,EvenName,EventDetails,UserResponsible,Request-ID,Session-ID)),docvalue_fields:\u21(%27@timestamp%27),query:(bool:(filter:\u21(),must:\u21((match_all:()),(range:(%27@timestamp%27:(format:epoch_millis,gte:starttime,lte:endtime)))),must_not:\u21(),should:\u21())),script_fields:(),sort:\u21((%27@timestamp%27:(order:desc,unmapped_type:boolean))),stored_fields:\u21(%27@timestamp%27,fields.logtype,%27Source%20IP%27,EvenName,EventDetails,UserResponsible,Request-ID,Session-ID),version:\u21t),index:%27typeX*%27),title:typeX,type:search)' -H 'Origin: http://10.102.12.32:5601' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' -H 'kbn-version: 6.3.2' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36' -H 'Proxy-Authorization: Basic cHJveHk6Z2RjaGluYXByZA==' -H 'Content-Type: application/json;charset=UTF-8' -H 'Accept: application/json, text/plain, */*' -H 'Referer: http://10.102.12.32:5601/app/kibana' -H 'Proxy-Connection: keep-alive' --data-binary '{}' --compressed --insecure"

#预先定义要生成的文件名以.csv结尾
download_name='download.csv'
#类型
typeX='bit-audit-log'
#时间戳， 以当前时间为截止时间，往前减, day为往前推的天数， x为转化后的秒数
day=7
x=day*24*60*60
starttime=str((int(time.time())-x)*1000)
endtime=str(int(time.time())*1000)
#starttime=str(1587774321446)
#endtime=str(1587775221446)
print(endtime,str(int(time.time()*1000)))
#完成日期类型动态参数替换
cmd=cmd.replace('starttime',starttime).replace('endtime',endtime).replace('typeX',typeX)

print(cmd)
b=os.popen(cmd)
#获取kibana返回值中的生成的动态文件名
filename=b.readlines()[0].split('download')[1][1:25]
print('***************************')
print(filename)
#准备开始下载
url="http://10.102.12.32:5601/api/reporting/jobs/download/"
url2=url+filename
print(url2)
bool0=1
while bool0:
    #c=os.popen(cmd2)
    r = requests.get(url2)
    with open(download_name, "wb") as code:
        code.write(r.content)
    fsize=os.path.getsize(download_name)
    print('fsize:',fsize)
    if fsize<100:
        print('<100', fsize,type(fsize))
        print('wait...')
        time.sleep(5)
        #a=input('a')
    else:
        print('else',fsize,type(fsize))
        #b=input('b')
        print('End')
        break
        bool0=0

print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')

#最后这段时显示下载后的文件， 可以不要，全注释掉
cmd3='cat '+download_name
t=os.popen(cmd3)
print(t.readlines())
