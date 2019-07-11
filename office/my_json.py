import json
import sys
def writejson(file,key,value):

#记录历史，写json文件的方法

    try:

        with open(file,"r") as f:

            load_dict = json.load(f)

    except:

        load_dict={}


    load_dict[key]=value
    print(load_dict)

    with open(file, 'w') as f:
        json.dump(load_dict, f, ensure_ascii = False, indent = 2)

def readjson(file,key):
    
    with open(file,"r") as f:

        load_dict = json.load(f)
    #print(load_dict)

    return load_dict[key]

writejson('config.ini','中文key3','日文value3')
x=readjson('config.ini','中文key3')
print(x)
