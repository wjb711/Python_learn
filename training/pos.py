import os,sys
directory_pos='c:/temp/pos'
directory_neg='c:/temp/neg'
os.chdir('c:/temp/')
def pos():
    with open("pos.txt","w") as f:
        for b in os.listdir(directory_pos):
            print ('pos'+'/'+b+' 1 0 0 136 36')

            f.write('pos'+'/'+b+' 1 0 0 136 36'+'\n')
def neg():
    with open("neg.txt","w") as f:
        for b in os.listdir(directory_neg):
            print ('pos'+'/'+b+'\n')

            f.write('neg'+'/'+b+'\n')
pos()
neg()
os.system('opencv_createsamples.exe -info pos.txt -bg bg.txt -num 1400 -vec pos.vec')
print ('done')
#os.system('opencv_traincascade.exe -data dt1 -vec pos.vec -bg bg.txt -numPos 1400 -numNeg 1964 -numStages 16 -precalcValbufSize 2000 -precalcdxBufSize 4000 -featureType LBP -w 100 -h 100')
#print ('done2')
os.system('opencv_haartraining.exe -data dt -vec pos.vec -bg neg.txt -numPos 1400 -numNeg 1964 -numStages 16 -precalcValbufSize 2000 -precalcdxBufSize 4000 -featureType LBP')
print ('done2')

