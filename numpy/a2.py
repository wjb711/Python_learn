import numpy as np
f=open('names.txt')
d=np.zeros((3,5), dtype="<U30")
x=0
y=0
for i in f.readlines():
    d[x][0],d[x][1],d[x][2],d[x][3]=i.split(':')
    x=x+1

print (d[:,2].sort())
f.close()
