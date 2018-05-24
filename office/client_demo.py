import socket
import getpass
import subprocess
import random
import sys
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 82))
psd='123adrtdrtdrtdr'
client.send(psd.encode('utf-8'))
back_msg = client.recv(1024)
client.close()
#print psd //避免出现差错忘记密码 先在本地打印 
