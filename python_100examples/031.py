'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
#Mo,Tu,We,Th,Fr,Sa,Su

st=input('1st:')
if st=='M':
    print ('Monday')
elif st=='W':
    print ('Wednesday')
elif st=='F':
    print ('Friday')
elif st=='T':
    st2=input('2nd:')
    if st2=='u':
        print ('Tuesday')
    elif st2=='h':
        print ('Thursday')
elif st=='F':
    print ('Friday')
    


