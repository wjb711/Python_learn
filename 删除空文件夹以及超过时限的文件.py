import os,datetime,sys
#历遍当前目录，a为目录，c为文件，b文件夹
path='./'
for a,b,c in os.walk(path):
    #如果目录为空，则删除空目录
    for b0 in b:
        #print (a)
        if not os.listdir(a+'/'+b0):
            
            print (a+'/'+b0)
            print ('empty folder, will be removed')
            os.rmdir(a+'/'+b0)
    #删除对应日期内的文件， 例如文件名成为aaa 2016-01-01 101010.xls, 2016-01-01超过某一数值， 删除
    #c0指对应的单个文件
    #c00指取出的日期（str）
    #c01指把c00由str转为日期格式
    for c0 in c:
        c00=c0.split('.',2)[-2].split(' ',2)[-2]
        c01=datetime.datetime.strptime(c00,"%Y-%m-%d")
        if (datetime.datetime.now()-c01).days >int(sys.argv[1]):
            print ('yes')
            print (c00)
            print (a+'/'+c0)
            #os.remove(a+'/'+c0)
    #print (a,b,c)
