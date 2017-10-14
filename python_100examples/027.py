'''

题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''
list=[]
list=input('hello:')
print (list)
len=len(list)
print (len)
#print (list[3])
for i in range(0,len):
    #print (len-i)
    print (list[len-i-1])

