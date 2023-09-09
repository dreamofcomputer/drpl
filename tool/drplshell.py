import os


print("DRPLshell 1.0\ndreamofcomputer")

while True:
    text=input("ds>")
    if "new" in text:
        text=text.replace("new ","")
        path=input("path>")
        os.mkdir(path+"\\"+text)
        os.system("copy drpl.py "+path+"\\"+text)
        os.system("copy dlib.py "+path+"\\"+text)
        os.system("copy drcode.txt "+path+"\\"+text)
        os.system("copy runItem.bat "+path+"\\"+text)
        print("new drpl item ok")
    
    if "run" in text:
        text=text.replace("run ","")
        os.system("start "+text+"\\runItem.bat")
    
    if "help"==text:
        print("1. new+[Item name]\n2. run+[Item name]\n3. help\n4. exit")
    
    if text=="exit":
        break
    