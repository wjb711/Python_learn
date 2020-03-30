from ping3 import ping, verbose_ping
import time,datetime
import json
import shutil


def writejson(ip):
#记录历史，写json文件的方法
    try:
        with open('./'+ip+'/data/min/'+date+".json","r") as f:
            load_dict = json.load(f)
    except:
        load_dict=[]


    dict0={}
    dict0['tmp']=str(tmp)
    dict0['hmt']=str(hmt)
    dict0['time']=str(time0)
    load_dict.append(dict0)
    with open('./'+ip+'/data/min/'+date+".json","w") as f:

        json.dump(load_dict,f)


def ping_rate(ip):
    sum0=0
    y0=0
    n0=0
    starttime=time.time()
    endtime=starttime+60
    while time.time()<=endtime:
        x=ping(ip,unit='ms')
        print(ip,x)
        if x is None:
            print('lost')
            n0=n0+1
        
        else:
            sum0=sum0+x
            y0=y0+1


    
    #print(w)
    print(int(sum0/y0),y0,n0,round(n0/(y0+n0)*100,2))
    return int(sum0/y0),round(n0/(y0+n0)*100,2)

if __name__=='__main__':

    ip=input("请输入要监测的IP:")
    #shutil.ignore_patterns(*patterns)
    src='./web'
    dst=ip
    try:
        shutil.copytree(src, dst, symlinks=False, ignore=None)
    except:
        pass
    while True:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        #tmp,hmt=1,1
        
        tmp,hmt=ping_rate(ip)
        #print(time,rate)
        time0 = datetime.datetime.now().strftime("%H:%M")
        writejson(ip)

