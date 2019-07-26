#注意先安装python-gnupg后Lib\site-packages下gnupg.py要手动改下，1483行改成always_trust=True
import os
import gnupg
import sys
print('location:',sys.argv[1])

#gpg = gnupg.GPG(gpgbinary='C:\\test\\gpg.exe',gnupghome='new')
gpg = gnupg.GPG(gpgbinary=sys.argv[1])
recipients=[]
for asc_file in os.listdir('./'):
    if asc_file.endswith('.asc'):
        with open(asc_file,'r') as f:
            gpg.import_keys(f.read())
        keys=gpg.scan_keys(asc_file)
        try:
            email_address=keys[0]['uids'][0].split('<')[1][:-1]
            print("*****************",email_address)
            
            recipients.append(email_address)
        except:
            pass
print('recipients:',recipients)
##print('x:',x,dir(x),dir(x.gpg))
#print('here:')
print(gpg.list_keys())
#keys=gpg.scan_keys('1.asc')
#email_address=keys[0]['uids'][0].split('<')[1][:-1]
#print(keys,type(keys),keys[0]['uids'][0].split('<')[1][:-1])
#data123='hello, china123'
recipients0='silvia.citro@gdm.de'

for file in os.listdir('./'):
    if file.endswith('.asc') or file.endswith('.pgp') or file.endswith('.gpg') or file.endswith('.bat') or file.endswith('.py') or os.path.isdir(file):
        pass
    else:
        print(file)
        with open(file,'rb') as f:
            encrypted_ascii_data = gpg.encrypt_file(f, recipients, output=file+'.pgp')
            print(encrypted_ascii_data,encrypted_ascii_data.ok,encrypted_ascii_data.status)
