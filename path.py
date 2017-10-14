import os
print (os.getenv("PATH"))
PATH=os.getenv("PATH")+';C:\\CV\\'
os.putenv=PATH
print (PATH)
