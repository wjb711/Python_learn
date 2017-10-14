'''
需求来自于需要替换两百个word文档中的关键词,做之前发现有个python-docx的
后来发现只支持docx,不支持doc
另外要注意win32这个插件，貌似只支持绝对路径，不支持相对路径，也有可能是word这个程序的问题。
如何使用？把此脚本复制到word的文件夹中， 即可替换所有的doc文件， 甚至是子文件夹中的doc也会一并替换
会提示输入old 原始字段， new，新字段， 一次只能替换一个
'''

import os
from win32com import client

#os的作用是把相对路径转化为绝对路径， win32com负责word
old=input('old:')
new=input('new:')

#定义老词，替换的新词
path='./'
#定义路径
app = client.Dispatch('Word.Application')
#定义word

#下面的a，b，c分别代表本地路径，文件夹名称，和子文件名称集合，这里使用os.walk就是用历遍所有的子目录
for a,b,c in os.walk(path):
    for c0 in c:
        
        abs=os.path.abspath(path)
        abc=(abs+a+"\\"+c0).replace('./','\\')
        #abs是初步转换出来的绝对路径，abc是最终的绝对路径
        if c0.endswith(".doc"):
        #如果是word，doc格式
            if c0.startswith("~"):
            #打开的word会有一个~$的隐藏文件，需要排除
                continue
        
            print (abc)
            doc=app.Documents.Open(abc)
            #打开word
            #print(os.path.abspath("aa1.doc"))
            app.Visible = False
            app.ScreenUpdating = False
            #不显示word程序
            app.Selection.Find.Execute(old, False, False, False, False, False, True, 1, True, new, 2)
            #替换
            doc.Save()
            #保存文档
            doc.Close()
            #关闭文档
app.Quit()
#退出word程序
