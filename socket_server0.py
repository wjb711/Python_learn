import socket
import time
server=socket.socket()
server.bind(('127.0.0.1',83))
server.listen(10)
while True:
    conn, address=server.accept()
    #conn.send('Hello,welcome to Test sytem'.encode('utf-8'))
    #conn.recv(1024)
    #time.sleep(30)
    #conn.send('\nPlease type some letters here:'.encode('utf-8'))
    #time.sleep(5)
    #x=conn.recvfrom(2048)
    while True:
        try:
            data = conn.recv(1024) # 接收1024个字节
        except:
            print('break')
            break
        print(data)
        if data:
            print(data.decode('utf-8'))
            print(data, type(data))
            x=('hello'+data.decode('utf-8')).encode('utf-8')
            conn.sendall(x)
            #print('yes')
        else:
            break

    #y=conn.recv(1024)

    #print(y)
conn.close()
