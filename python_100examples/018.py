total1=0
for y in range(1,4+1):
    
    list=[]
    for i in range(0,y):
        a=10**i
        list.append(a)
    total=0
    for x in list:
        total=total+x
    total1=total1+total
print (total1)

