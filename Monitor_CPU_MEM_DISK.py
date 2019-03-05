import datetime,socket,time,psutil,sys
intervaltime=int(sys.argv[1])
value=int(sys.argv[2])
location=sys.argv[3]
def monitor():
    
    now=datetime.datetime.now()
    
    time0=now.strftime("%Y-%m-%d %H:%M:%S")
    day=now.strftime("%Y-%m-%d")
    #print(now)
    hostname=socket.gethostname()
    cpu=psutil.cpu_percent(interval=0.5)

    mem = psutil.virtual_memory()
    mem0=round((mem.used/mem.total)*100,1)

    disk=psutil.disk_usage('C:\\')
    disk0=disk.percent
    return day,time0,hostname,cpu,mem0,disk0
#print(monitor())
while True:
    time.sleep(intervaltime)
    day,time0,hostname,cpu,mem0,disk0=monitor()
    #now=datetime.datetime.now()
    with open("./logs/"+day+'_'+hostname+'.log',"a") as f:
        f.write(time0+" "+hostname+" CPU: "+str(cpu)+" Mem: "+str(mem0)+" disk: "+str(disk0)+'\n')
    if cpu>value or mem0>value or disk0>value:
        print (location+'/'+day+'.log')
        with open(location+'/'+day+'.log',"a") as f:
            f.write(time0+" "+hostname+" CPU: "+str(cpu)+" Mem: "+str(mem0)+" disk: "+str(disk0)+'\n')
