'''
<<<<<<< HEAD
斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........
自然中的斐波那契数列
自然中的斐波那契数列
这个数列从第3项开始，每一项都等于前两项之和。
'''
=======
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''
def fib(n):
    list=[0,1]
    for i in range(2,n):
        list.append(list[i-2]+list[i-1])
    return list[n-1]
print (fib(10))
    
>>>>>>> origin/master
