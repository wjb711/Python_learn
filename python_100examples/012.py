'''
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数
'''
for i in range(2,200):
    list=[]
    for z in range(2,i):
        list.append(i%z)
    if 0 not in list:
        print (i)
        
