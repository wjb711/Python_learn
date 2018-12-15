#先登录一环境监控系统，获取cookies后在访问温度湿度数值的网页，并保存为excel格式
import urllib.request

import http.cookiejar

import datetime,re,os
#取当前时间前16位
now=datetime.datetime.now()
now1=str(now)[:16]


cookie=http.cookiejar.CookieJar()
#实例化一个全局opener
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
# 获取cookie


r=opener.open("http://yourserver/cgi-bin/login.cgi?user_name=wjb711&user_password=sdsfsdfsdlan=zh&op_Type=1&rand_code=0")
# 访问主页 自动带着cookie信息

#办公机房
url1='http://yourserver/cgi-bin/p101_refresh_page.cgi?_equip=12&_op_type=0&_element_list=6|92;300;0,2@93;300;0,17@94;700;0,2@95;700;0,17@96;701;0,3@97;701;0,18@&sand=0.5109610645004223'
#生产机房
url2='http://yourserver/cgi-bin/p101_refresh_page.cgi?_equip=-99&_op_type=0&_element_list=12|144;300;0,9@145;300;0,5@146;700;0,5@147;700;0,13@148;701;0,72@149;701;0,68@150;700;0,17@151;700;0,9@152;701;0,80@153;701;0,76@154;300;0,13@155;300;0,17@&sand=0.6098958789874185'
#url1="http://yourserver/cgi-bin/p101_refresh_page.cgi?_equip=13&_op_type=0&_element_list=3|65;700;0,2@66;701;0,3@67;901;0,-1@&sand=0.48388160580111106"

result1 = opener.open(url1).read().decode()
result2 = opener.open(url2).read().decode()
x=re.split('[|,~;:]', result1)
y=re.split('[|,~;:]', result2)
#result.status
print ("当前时间",now1)
print (x[13],x[14]+'°C',x[17],x[18]+'°C',x[21],x[22]+'%',x[25],x[26]+'%')
print (y[13],y[14]+'°C',y[17],y[18]+'°C',y[21],y[22]+'%',y[25],y[26]+'%',y[29],y[30],y[33],y[34],y[37],y[38],y[41],y[42])


filename='温湿度监控.csv'
def write():
    with open(filename,'a+') as f:
        f.write(now1+','+x[14]+'°C'+','+x[18]+'°C'+','+x[22]+'%'+','+x[26]+'%'+',')
        f.write(y[14]+'°C'+','+y[18]+'°C'+','+y[22]+'%'+','+y[26]+'%'+','+y[30]+'°C'+','+y[34]+'°C'+','+y[38]+'%'+','+y[42]+'%'+','+'\n')
if os.path.exists(filename):
    write()
else:
    with open (filename,"w+") as f:
        f.write('日期和时间'+','+'办公机房温度0'+','+'办公机房温度3'+','+'办公机房湿度0'+','+'办公机房湿度3'+','+'生产机房温度11'+','+'生产机房温度31'+','+'生产机房湿度21'+','\
                +'生产机房湿度11'+','+'生产机房温度41'+','+'生产机房温度21'+','+'生产机房湿度41'+','+'生产机房湿度31'+'\n')
    f.close()
    write()
