def os_cmd(cmd):
    import subprocess
    #cmd='ping www.baidu.com'
    p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, bufsize=1)
    result=[]
    for line in iter(p.stdout.readline,b''):
        print (str(line,encoding = "utf8"))
        result.append(str(line,encoding = "utf8").replace('\r\n',''))
    #out=p.stdout.readlines()
    #print(out)
    p.stdout.close()

    p.wait()
    #print('*****************************')
    return result
cmd='dir'
os_cmd(cmd)
