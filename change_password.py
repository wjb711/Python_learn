#用户自动更改账号密码的python脚本，实现用户点下链接，即可自动改为
#当前日期.com的密码，例如20180502.com
import getpass
import datetime
import easygui as g
import subprocess

#获取用户名
user = getpass.getuser()
#当前日期
now=datetime.datetime.now()
date0=str(now)[:10].replace('-','')
password=date0+'.com'
print (password)
#命令行修改密码
subprocess.Popen(['net', 'User', user, password])
#弹出提示
g.msgbox('您的密码已更新为'+password+'请牢记')
