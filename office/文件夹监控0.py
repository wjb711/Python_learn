import os
import time,datetime
monitor_dir = "./opt/"

#print(now_file)
def tree(folder):
    dict0={}
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            if 'ff' in name:
                pass
            else:
            #print(os.path.join(root, name))
            #print(root,'***',name)
                dict0[root+'/'+name]=name
    return dict0
before=tree(monitor_dir)
log='1.log'
while True:
#print(x)
    time.sleep(5)
    after=tree(monitor_dir)
    added=[f for f in after if not f in before]
    removed=[f for f in before if not f in after]
    now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if added:
        print (now,"Added:",",".join(added))
        with open(log,'r') as f:
            x=f.readlines()
        with open('1.log','w') as f:
            f.write(now+" Added:"+",".join(added)+'\n')
            for item in x:
                f.write(item)
    if removed:
        print (now,"Removed:",",".join(removed))
        with open(log,'r') as f:
            x=f.readlines()
        with open('1.log','w') as f:
            f.write(now+" removed:"+",".join(removed)+'\n')
            for item in x:
                f.write(item)
        #with open('1.log','r+') as f:
            #f.write(now+"Added:"+",".join(removed))
    before = after
    
    
