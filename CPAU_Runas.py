#this is a python script based on 'cpau.exe' to to use as Runas function
#you have to download cpau.exe
#if you do not have easygui or datetime installed
#you have to install it by 'pip install easygui '
#you have to install it by 'pip install datetime '
#for CPAU.exe ,you can download it here https://github.com/wjb711/Python_learn/blob/master/office/CPAU.exe
#for CPAU usage, you can find help information here http://www.joeware.net/freetools/tools/cpau/usage.htm
#for python download, you can find it here https://www.python.org/downloads/

import os
import easygui as g
import getpass
import socket
import datetime
import sys

now=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
app='CPAU.exe'
x=os.popen(app).readlines()
while x==[]:
    g.msgbox('this programe is used for run as function of windows, you need to download CPAU.exe \
            from here https://github.com/wjb711/Python_learn/blob/master/office/CPAU.exe  \
            1st，copy '+app+'copy to folder c:\windows\system32\ ')
    
    
#while not os.path.exists(now+'.exe'):

#print ('x',x.read())
print (dir(getpass))
hostname = socket.gethostname()
#print (hostname)

print (getpass.getuser())
file_path = g.fileopenbox(title='2nd，select exe or bat files')
file_path0 = file_path.replace('\\','/')
dirname,filename=os.path.split(file_path0)
print(filename)
#input(a)
username=g.enterbox(title='3rd，domain\ username',msg='for example "accounts\wanjianb"')
password=g.passwordbox(title='4th，enterpassword')

x1=os.popen(app+' -u '+username+' -p '+password+' -ex '+file_path+' -enc -file '+filename+'.txt').readlines()
print (x1)

with open(filename+'.bat', 'w') as f:
    f.write('CPAU.exe -dec -file '+'.\\'+filename+'.txt'+ ' -lwp'+'\n')
    f.write('pause')
g.msgbox('Done, please check '+filename+'.bat')
os.system(filename+'.bat')
