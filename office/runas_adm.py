def authtication_adm():
    import getpass
    import os
    import time
    import sys
    #是否存在lsrunas.exe这个插件
    if os.path.exists('./lsrunas.exe'):
        pass
    else:
        print('当前路径下没有发现lsrunas.exe,请重新下载https://www.softpedia.com/get/System/System-Miscellaneous/LSrunas.shtml#download')
        sys.exit()
    获取当前用户名
    username1=getpass.getuser()
    print('当前登录用户为:',username1)
    if username1.startswith('adm'):
        print('是管理员账号,adm account')
            
        pass
    else:
        print('当前非管理员账号，请输入adm开头的管理员账号')
        admusername=input('admusername:')
        password=getpass.getpass('password:')
        filename=sys.argv[0]
        print('filename',filename)
        path0=os.getcwd()
        command='lsrunas.exe /user:{} /password:{} /domain:accounts.intern /command:"python {}" /runpath:{}'.format(admusername,password,filename,path0)
        print(command)
        print(os.popen(command,'r').read())
        print('here we go!')
        sys.exit()
