import os,sys,codecs
#freefilesync的函数，主要用来更改源目录和目的目录
def freefilesync_mask(item):
    #s =item
    #print (s)
    #if isinstance(item, unicode):
    #    item = item.encode('utf-8')
    #item=item.encode().decode()
    print (item)
    #读取BatchRun.ffs_batch作为freefilesync的脚本文件
    f=codecs.open('BatchRun.ffs_batch','r+',encoding='utf-8')
    flist=f.readlines()
    #第40行变更为源目录，41行变更为目的目录
    flist[40]='		<Left>//'+item+'/'+a1+'</Left>\n'
    flist[41]='		<Right>'+a2+item+'</Right>\n'

    #判断目的目录有没有机器名对应的目录，没有的化创建一个
    if os.path.exists(a2+item):
        pass
    else:
        os.makedirs(a2+item)
    print ('from',flist[40],'to',flist[41])
    #print (flist)
    f=codecs.open('BatchRun.ffs_batch','w+',encoding='utf-8')
    f.writelines(flist)
    f.close()
    #运行freefilesync
    os.system('BatchRun.ffs_batch')
#freefilesync_mask('item1dsfsdfdsgsdg')
#打开config.ini
f=open('config.ini', 'r')
#location=f.readlines()
#print (location)
#显示开始
print ('**********start****************')
#读取配置文件的第一行作为同步源目录例如\\hostname\GD\logs\
a1=f.readlines()[0][:-1]
f=open('config.ini', 'r')
print ('1st line is ',a1)
#读取第二行作为同步的目的目录，例如d:\syslog\logs\hostname
a2=f.readlines()[1][:-1]
print ('2nd line is ',a2)
f=open('config.ini', 'r')
#从配置文件第三行起，读取作为机器名列表
for line in f.readlines()[2:]:
    item=line[:-1]
    print (item)
    #调用freefilesync开始同步
    freefilesync_mask(item)
#显示结束
print ('***********end****************')


