import re,cv2

def grep(keyword,text):
    for i in text:
        #print (type(text),i,type(i))
        if re.search(keyword,i)==None:
            pass
        else:
            print (i)


text="hello, world\
this is my 1st time to earth\
please help me\
thanks a lot"

#print (re.search('www','qw1ww w1ww 123'))
with open('1.txt','r') as f:
    text=f.readlines()
#text=['aaa','bbb','ccc']
text=dir(cv2)
grep('cv',text)
#print (re.search('bbb1','bbb'))
