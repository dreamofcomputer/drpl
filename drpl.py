#import
import linecache
import dlib

rh=2  #因为程序第一行为start{,所以用2
line1=linecache.getline(r"drcode.txt",1)
varlist=["","","","",""]
if line1=="start{\n":
    while True:
        getlines=linecache.getline(r"drcode.txt",rh)
        revar=dlib.drpllib(getlines)

        if revar=="out":
            getprint=linecache.getline(r"drcode.txt",rh+1)
            getprint=getprint.replace('\n', '')#去掉\n(用""替换掉"\n")
            
            if "string&" in getprint:
                getprint=getprint.replace(' ', '')
                getprint=getprint.replace('string&', '')
    
                print(getprint)
    
            if "var&" in getprint:
                getprint=getprint.replace(' ', '')
                getprint=int(getprint.replace('var&', ''))
    
                print(varlist[getprint])
            
        if revar=="end":
            break

        if revar=="in":
            intvar=getlines.replace('in{', '')
            intvar=intvar.replace('\n', '')#保留待输入变list储存器部分
            intvar=int(intvar)
            getin=linecache.getline(r"drcode.txt",rh+1)
            getin=getin.replace('\n', '')#去掉\n(用""替换掉"\n")

            #保留字符串
            if "string&" in getin:
                getin=getin.replace(' ', '')
                getin=getin.replace('string&', '')
                varlist[intvar]=getin

            if "input&" in getin:
                getin=getin.replace(" ","")
                getin=getin.replace("input&","")
                varlist[intvar]=input(getin)

        rh=rh+1
a=input("\nend")