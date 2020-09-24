import os
a=input("enter a file name")
m=os.path.splitext(a)
if m[1]==".py":
    print("the extension is python")
elif m[1]==".pdf":
    print("pdf")
else:
    print("is nothing")
      
