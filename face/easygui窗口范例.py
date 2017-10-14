import easygui
from easygui import msgbox, multenterbox

  = "3.jpg"
msg = "是否加入到人脸识别库中?"
choices = ["Yes","No"]
reply = easygui.buttonbox(msg, image=image, choices=choices)
if reply=="No":
    print("no")
else:
    print("yes")
    flavor = easygui.enterbox("请输入名字（必须是英文（拼音），不能有空格和特殊符号）") 
    easygui.msgbox ("您输入了： " + flavor)
    


