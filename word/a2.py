import easygui as g
msg = 'Enter your personal information'
title = 'Credit Card Application'
fieldNames = ['来源','数量','备注']
fieldValues = []
fieldValues = g.multenterbox(msg,title,fieldNames)
print(fieldValues[1])
