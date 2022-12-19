#import
import linecache
import dlib
import os

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

        if revar=="jump":
            jumpnumber=getlines.replace(" ","")
            jumpnumber=jumpnumber.replace("\n","")
            jumpnumber=jumpnumber.replace("jump[","")
            jumpnumber=int(jumpnumber.replace("]",""))
            rh=jumpnumber-1    #最后会加1，所以减1

        if revar=="=if":
            ifvar1=getlines.replace("=if{","")
            ifvar1=ifvar1.replace("\n","")
            ifvar1=ifvar1.replace(" ","")
            ifvar2=linecache.getline(r"drcode.txt",rh+1)
            ifvar2=ifvar2.replace(" ","")
            ifvar2=ifvar2.replace("\n","")

            #ifvar1
            if "var&" in ifvar1:
                ifvar1=varlist[int(ifvar1.replace("var&",""))]

            if "string&" in ifvar1:
                ifvar1=ifvar1.replace("string&","")

            #ifvar2
            if "var&" in ifvar2:
                ifvar2=int(ifvar2.replace("var&",""))

            if "string&" in ifvar2:
                ifvar2=ifvar2.replace("string&","")

            #if
            if ifvar1==ifvar2:
                ifjumprh=linecache.getline(r"drcode.txt",rh+2)
                ifjumprh=ifjumprh.replace("ifjump[","")
                ifjumprh=ifjumprh.replace("]","")
                ifjumprh=ifjumprh.replace("\n","")
                ifjumprh=int(ifjumprh.replace(" ",""))
                rh=ifjumprh-1
        
        if revar=="console":
            inputcmd=getlines
            inputcmd=inputcmd.replace("\n","")
            inputcmd=inputcmd.replace(" ","")
            inputcmd=inputcmd.replace("console[","")
            inputcmd=inputcmd.replace("]","")
            os.system(inputcmd)

        rh=rh+1
a=input("\nend")