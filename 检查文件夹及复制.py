import os,shutil
location='c:/Users/'
location1='/AppData/Roaming/SAP/LogonServerConfigCache/'
location2='/AppData/Roaming/SAP/'
for i in os.listdir(location):
    if os.path.isdir(location+i):
        print (i," is folder")
        if os.path.exists(location+i+location1):
            print (i,"has SAP already")
        else:
            print (location+i+location2)
            shutil.copytree('c:/temp/SAP/',location+i+location2)
            

