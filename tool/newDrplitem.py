import os
itemname=input("new drpl item name>")
path=input("new drpl item path>")
os.mkdir(path+"\\"+itemname)
os.system("copy drpl.py "+path+"\\"+itemname)
os.system("copy dlib.py "+path+"\\"+itemname)
os.system("copy drcode.txt "+path+"\\"+itemname)
os.system("copy runItem.bat "+path+"\\"+itemname)
end=input("new drpl item ok")