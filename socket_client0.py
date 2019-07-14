import socket
import time
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client)
 
 
client.connect(('127.0.0.1', 83))
 
while True:
    data = input('input >>>')
    if not data:  # 如果数据为空，继续输入
        continue
    client.send(data.encode('utf-8'))  # 发送数据
    time.sleep(1)
 
    data = client.recv(1024)   # 接收数据
    print('接收数据 =' , data.decode())
 
client.close()  # 关闭
