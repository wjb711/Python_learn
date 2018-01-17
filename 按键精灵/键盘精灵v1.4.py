import pyautogui as p

import easygui as g

import os,time

#print (os.listdir('./'))

print ('键盘精灵，开发者:王剑波 email:10054053@qq.com')

#设定热键的集合

hotkey=['win','ctrl','alt','esc','left','right','up','down','enter','tab','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','del']

selectfile={}

for i in os.listdir('./'):

    if i.endswith('.bmp'):

        #pass

        #print (i)

        try:

            x, y = p.locateCenterOnScreen(i)

            print ('pic is found',i)

            print (x,y)

            

            p.click(x, y)

            time.sleep(0.5)

        except:

            print ('not found pic',i)

            pass

        #print (x,y)

        #p.hotkey('win')

    elif i.endswith('.txt'):

        f=open(i,'r')

        lines=f.readlines()

        for line in lines:

            try:

                word,times=(line.replace('\n','')).split('*',1)

                #print ('times is :',times)

            except:

                times=1

                word=line.replace('\n','')

           

            #print (word,'hell0')

            if word=='' or word.startswith('#'):

                pass

            elif word in hotkey:

                for t in range(int(times)):

                    print (word)

                   

                    p.hotkey(word)

                    time.sleep(0.6)

                   

            elif word.startswith('pause'):

                print ('暂停时间')

                time.sleep(int(word.replace('pause','')))

            elif word.startswith('selectfile'):

                try:

                    print (selectfile[word])

                    p.typewrite(selectfile[word])

                except:

                    filename=g.fileopenbox()

               

                    selectfile[word]=filename

               

            elif '+' in word:

                if word.split('+')[0] in hotkey:

                    if len(word.split('+'))==3:

                        x,y,z=word.split('+')

                        p.hotkey(x,y,z)

                    elif len(word.split('+'))==2:

                        x,y=word.split('+')

                        p.hotkey(x,y)

                else:

                    p.typewrite(word)

            else:

                print (word)

                p.typewrite(word)

            time.sleep(0.6)

        f.close()
