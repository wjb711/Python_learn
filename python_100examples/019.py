
for i in range(1,1000):
    total=0
    for y in range(1,i):
        if i%y==0:
            #print ('i is ',i)
            total=total+y
            #print ('total is ',total)
    if i==total:
        print ('*****************',i,'****************')
            
