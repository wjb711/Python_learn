import datetime,time,糗事百科抓文字
import datetime,time
#设定开始时间start_time
def timer():
    sched_time = datetime.datetime(2017, 8, 19, 11, 53, 50)
    #间隔时间
    timedelta=datetime.timedelta(minutes=5)
    #取当下时间
    now = datetime.datetime.now()
    #判断是否开始时间已错过,如果结果为负数，则提示错误
    if str(sched_time-now)[0]=='-':
        print ('开始时间已经错过，请重新调整开始时间')
    else:
        while True:
            now = str(datetime.datetime.now())[:-7]
            if now==str(sched_time):
                print (sched_time)
                sched_time=str(datetime.datetime.now()+timedelta)[:-7]
                print (sched_time)
                print ('请在这里开始你的程序')
                糗事百科抓文字.main()
            time.sleep(1)
            print (now)
if __name__=='__main__':
    timer()
        
