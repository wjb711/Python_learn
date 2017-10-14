"""
this is for what is config.ini
**************
arg1:hello5
arg2:hello5
3:c
4e:5c
arg4:cv2
*********
"""
with open('config.ini', 'r') as f:
    result = dict(line.strip().split(':') for line in f if line)
print(result['1'])
print(result['arg4'])

