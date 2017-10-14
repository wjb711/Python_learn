# -*- coding: utf-8 -*-
# 引入Speech SDK
from aip import AipSpeech
import json
import recorder
import os,sys
print ('start now')


global ask
ask=u'中国'
print (ask)
#ask=lists[0]
feedback=os.popen('py -2 p3.py '+ask).readlines()
print ('py -2 p3.py '+ask)
for f in feedback:
    print (f.decode())
print ('end')


