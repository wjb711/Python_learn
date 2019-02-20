from w3lib.html import remove_tags
import os
import sys
keywords=sys.argv[1:]

print('此程序是为了快速搜索html文件中的关键词而做')
print('具体的使用方法是本程序.exe "关键词一" "关键词二" "关键词三" "关键词四"')
print('有问题联系王剑波')
print('\n')
print('本地搜索关键词为',keywords)
print('\n')
#b=remove_tags(a)
#print(b)

def grep(keyword,file):
    with open(file,'r') as f:
        x=f.read()
    #print(x)
    d=x.replace('<br>','\n')
    c=remove_tags(d)
    #print(type(c))
    f=c.split('\n')
    #print(c)
    for y in f:
        if keyword in y:
            #print(file+'> '+y)
            print(y)
           
for file in os.listdir('./'):
    if file.endswith('.html'):
        print("***********************< "+file+" >**************************")
        for keyword in keywords:
            #print(keyword)
            grep(keyword,file)
            #grep('Order file',file)
        print('\n','\n')

#print(os.getcwd())
a=input("任意键退出！")
