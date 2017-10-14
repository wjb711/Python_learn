import random,time
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id) #changing index changes voices but ony 0 and 1 are working here
#engine.say('萱萱学减法，二十道减法题，每题五分，现在开始')
engine.runAndWait()


def yuyin(text):
    
    engine.say(text)
    engine.setProperty('rate',120)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()
def huida():
    global b
    global s
    answer=int(input('答案：'))
    
    
    if answer==(b-s):
        yuyin('正确')
        yuyin(b-s)
        print (b-s)
    else:
        yuyin('错误,再来一次')
        huida()

i=1
while i<21:

    x=random.randint(11,99)
    y=random.randint(11,99)
    #print (s1,s2)
    if x>y:
        b=x
        s=y
    else:
        b=y
        s=x
    
    if b==s:
        continue
    if b%10 >=s%10:
        continue
    if b-s<10:
        continue
    else:
        engine.say('第')
        engine.say(i)
        engine.say('题')
        print (b,'-',s)
        yuyin(b)
        yuyin('减')
        yuyin(s)
        yuyin('等于')
        huida()

            
        print ('********************************************************')
        i=i+1

    
        
