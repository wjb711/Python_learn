import json
import os
import datetime
import shutil
import time
def readjson(file):
    try:

        with open(file,"r") as f:

            load_dict = json.load(f)

    except:

        load_dict={}
    #print(load_dict,load_dict['mail_server'])

    return load_dict
config=readjson('./config.ini')
print(config,type(config))
source=config['source']
dest=config['dest']
filetypes=config['filetypes']
time0=int(config['time'])
print(source,dest,filetypes)

now=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print(now)
while True:
    for file_type in filetypes:
        for file in os.listdir(source):
            if file.endswith(file_type):
                shutil.copyfile(source+file,dest+file+'_'+now+file_type)
    time.sleep(time0)


