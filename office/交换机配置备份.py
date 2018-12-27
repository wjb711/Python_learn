import paramiko
import datetime
import sys


def command(action,end):
    ssh_shell.sendall( action + '\n')
    lines = []
    while True:
        line = ssh_shell.recv(1024).decode()
        with open (now1+'@'+host+'.txt','a+') as f:
            f.write(line)
        print (line)

        if line[-1]==end:
            break;
        #lines.append(line)
    #print ('********')
 


#print ('****************************')
if __name__=='__main__':
    print ("欢迎使用本程序")
    print ("本程序的目的是为了实现自动备份cisco交换机的配置文件")
    print ('格式为 本程序.exe 服务器ip 用户名 password enable_password')
    print ('')
    now1=datetime.datetime.now().strftime('%Y%m%d%H%M')
    print (now1)
    client = paramiko.SSHClient()
    #client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    host=sys.argv[1]
    username=sys.argv[2]
    password=sys.argv[3]
    enable_password=sys.argv[4]
    
    # connect to client
    client.connect(host,22,username,password,allow_agent=False,look_for_keys=False)
    ssh_shell = client.invoke_shell()
    command('','>')
    command('enable',' ')
    command(enable_password,'#')
    command('terminal length 0','#')
    command('show run','#')   
