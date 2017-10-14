import os
from win32com import client
old=input('old:')
new=input('new:')
app = client.Dispatch('Word.Application')
for a in os.listdir():
    if a.endswith(".doc"):
        if a.startswith("~"):
            continue
        
        abs=os.path.abspath(a)
        print (a,abs)
        doc=app.Documents.Open(abs)
        #print(os.path.abspath("aa1.doc"))
        app.Visible = False
        app.ScreenUpdating = False

        app.Selection.Find.Execute(old, False, False, False, False, False, True, 1, True, new, 2)
        doc.Save()
        doc.Close()

app.Quit()
