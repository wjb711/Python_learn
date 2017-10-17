import os,sys,cv2
directory_pos='c:/temp/pos'
directory_neg='c:/temp/neg'
os.chdir('c:/temp/')
def resize(img,size):
    pic=cv2.imread(img)
    if pic.shape==(24,24,3):

        print ('y',pic.shape)
    else:
        re=cv2.resize(pic,(size,size))
        print ('n',pic.shape)
        cv2.imwrite(img,re)

i=0    
def pos_text():
    with open("pos.txt","w") as f:
        for b in os.listdir(directory_pos):
            if b.endswith('.jpg'):
                print ('pos'+'/'+b+' 1 0 0 136 36')

                f.write('pos'+'/'+b+' 1 0 0 136 36'+'\n')
                i=i+1
    return i
def neg():
    with open("neg.txt","w") as f:
        for b in os.listdir(directory_neg):
            print ('pos'+'/'+b+'\n')

            f.write('neg'+'/'+b+'\n')
def pos_resize():
    os.chdir('c:/temp/pos/')
    for b in os.listdir(directory_pos):
        if b.endswith('.jpg'):
            resize(b,24)
def neg_resize():
    os.chdir('c:/temp/neg/')
    for b in os.listdir(directory_neg):
        if b.endswith('.jpg'):
            resize(b,24)
p=pos_text()
pos_resize()
neg()
neg_resize()
os.system('opencv_createsamples.exe -info pos.txt -bg bg.txt -num 1400 -vec pos.vec')
print ('done')
#os.system('opencv_traincascade.exe -data dt1 -vec pos.vec -bg bg.txt -numPos 1400 -numNeg 1964 -numStages 16 -precalcValbufSize 2000 -precalcdxBufSize 4000 -featureType LBP -w 100 -h 100')
#print ('done2')
os.system('opencv_haartraining.exe -data dt -vec pos.vec -bg neg.txt -numPos 1400 -numNeg 1964 -numStages 16 -precalcValbufSize 2000 -precalcdxBufSize 4000 -featureType LBP')
print ('done2')

