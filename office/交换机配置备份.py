import paramiko
import datetime
import sys

#command 的意思是发送一个action指令，当遇到结束语end的时候停止 
def command(action,end):
    ssh_shell.sendall( action + '\n')
    lines = []
    while True:
        #抓取报文，原始为byte,转化为字符串str
        line = ssh_shell.recv(1024).decode()

        #追加写入日期+host名的txt文件中
        with open (now1+'@'+host+'.txt','a+') as f:
            f.write(line)
        print (line)

        #遇到定义好的end终止符，终止此函数
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

    #这个是去当前的日期加时间
    now1=datetime.datetime.now().strftime('%Y%m%d%H%M')
    print (now1)

    #定义连接
    client = paramiko.SSHClient()
    #client.load_system_host_keys()
    #不加这行会报主机不在known_host的错误
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #获取外部参数，1,2,3，4分别代表ip，用户名，密码，enable密码
    host=sys.argv[1]
    username=sys.argv[2]
    password=sys.argv[3]
    enable_password=sys.argv[4]
    
    # 建立链接
    client.connect(host,22,username,password,allow_agent=False,look_for_keys=False)
    ssh_shell = client.invoke_shell()
    command('','>')
    command('enable',' ')
    command(enable_password,'#')
    command('terminal length 0','#')
    command('show run','#')   
