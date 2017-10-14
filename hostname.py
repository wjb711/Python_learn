import os
#os.system("c:/windows/system32/NOTEPAD.EXE c:/TEMP/a1.txt")
#print ("done")
#p=subprocess.Popen(pname)
#location="c:/temp/20170618/20170618/"
location='./'
for i in os.listdir(location):
    if i.endswith(".exe"):
        print (i)
        mid=i[8:-4]
        os.makedirs(location+mid,exist_ok=True)
        os.rename(location+i,location+mid+'/'+i)
    #print (i)
    #print ('left:'+i[0:8])
    #print ('right:'+i[-4:-1]+i[-1])
    
    #print ('mid:'+i[8:-4])
    
    #i0=i
    #i1=i.replace('.zip','.rar')
    #print (i0,i1)
    #os.rename(location+i,location+mid+'/'+i)
    
#list=os.system("dir c:/temp")
#print (list)


