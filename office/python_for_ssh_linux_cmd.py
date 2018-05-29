import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='your IP', port=22, username='root',password='your password')
#CMD='pwd'
CMD='sh /nfs/TimeMachineBackup/scripts/syncnc.sh'
print('$ ' + CMD)
stdin, stdout, stderr = client.exec_command(CMD)
for line in stdout:
    print('> ' + line.strip('\n'))
print('Finished')
time.sleep(3)
CMD='date\n'
stdin, stdout, stderr = client.exec_command(CMD)
for line in stdout:
    print('> ' + line.strip('\n'))
#client.close()
print('Finished')
