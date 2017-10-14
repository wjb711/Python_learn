'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
def zys(N):
    #global N
    print ('n is ',N)
    if N==2:
        print (N)
    n=2
    for x in range(2,N):
        #print ( N ,'%',x,'=',N%x)
        if N%x==0:
            print (x)
            N=int(N/x)
            zys(N)
            break
        else:
            n+=1
            if N==n:
                print (N)
        
    


print (zys(32))
            
        
        
