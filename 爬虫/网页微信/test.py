import datetime,time
#设定开始时间start_time
sched_time = datetime.datetime(2017, 8, 19, 10, 53, 00)
#间隔时间
timedelta=datetime.timedelta(minutes=1)
#取当下时间
now = datetime.datetime.now()
#判断是否开始时间已错过,如果
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
        time.sleep(1)
        print (now)
        
    
