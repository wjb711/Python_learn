# -*- coding: cp936 -*-

"""
#本脚本的目的是单向单次同步
具体的方法是先读取配置文件
把源目录的文件做一个集合与前一次目录的集合做对比
对差异部分采取行动，例如同步或者上传下载。
"""

import sys,os,codecs
print ('start')
#sys.setdefaultencoding('utf-8')
def freefilesync_mask(item):
    #s =item
    #print (s)
    #if isinstance(item, unicode):
    #    item = item.encode('utf-8')
    #item=item.encode().decode()
    print (item)
    f=codecs.open('BatchRun.ffs_batch','r+',encoding='utf-8')
    flist=f.readlines()
    #flist[24]='                <Item>'+item+'</Item>\n'
    flist[40]='                <Left>\\PC-201704171154\Users</Left>'
    print (flist[40])
    print (flist)
    f=codecs.open('BatchRun.ffs_batch','w+',encoding='utf-8')
    f.writelines(flist)
    f.close()
    

#读取配置文件
with open('config.ini', 'r') as f:
    #配置文件以等号为分隔符
    config = dict(line.strip().split('=') for line in f if line)

#目标源为配置文件中的souce项
source=config['source']
#先定义两个空的集合之前和之后
set_before=set()
set_after=set()
#判断列表文件是否存在，如果没有，新建一个。

if os.path.isfile('filelist.txt'):
    pass
else:
    file1 = open("filelist.txt","w")
    file1.close()
#读取列表文件到集合1,set_before
file1 = open("filelist.txt","r")
for line in file1.readlines():
    line=line[0:-1]
    set_before.add(line)
#print ("set_before",set_before)
file1.close()
#把当前目录文件读作集合2，set_after并写入列表文件。
file1 = open("filelist.txt","w")
#print ("done")
for i in os.listdir(source):
    #print (i)
    set_after.add(i)
    file1.writelines(i+"\n")

file1.close() 
#当前的集合减去之前的集合， 就是要操作的集合  
set_fi=set_after-set_before
print (type(set_fi))
print(set_fi)
for d in set_fi:
    print (d)
    freefilesync_mask(d)
    os.system('BatchRun.ffs_batch')
    print ('done')

 
 

