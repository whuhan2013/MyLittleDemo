import os
import easygui as g
import sys
import chardet
path = 'C:/'
path='D:/Data/CProject/dataStruct/PAT/PAT'
path='F:/Workspaces'
path2='D:/Data/CProject'
path3='D:/WorkSpace/SoftWare/cocos2d-x-2.2.3/projects'
path4='F:/MyWrokspace'
iforjava=0;
iforcpp=0;
iforc=0;

for root, dirs, files in os.walk(path):
        #files=''.join(files)
        
        #print(type(files))
        for str1 in files:
                if 'java'==str1.split('.').pop():
                        print("Root = ", root, "dirs = ", dirs, "files = ", str1)
                        count= len(open(root+'\\'+str1,'rU',encoding= 'gbk').readlines())
                        iforjava=iforjava+int(count)
                        print('行数为:',count)

for root, dirs, files in os.walk(path2):
        #files=''.join(files)
        
        #print(type(files))
        for str1 in files:
                if 'c'==str1.split('.').pop():
                        print("Root = ", root, "dirs = ", dirs, "files = ", str1)
                        count= len(open(root+'\\'+str1,'rU',encoding= 'gbk').readlines())
                        iforc=iforc+int(count)
                        print('行数为:',count)
                if 'cpp'==str1.split('.').pop():
                        print("Root = ", root, "dirs = ", dirs, "files = ", str1)
                        count= len(open(root+'\\'+str1,'rU',encoding= 'gbk').readlines())
                        iforcpp=iforcpp+int(count)
                        print('行数为:',count)

for root, dirs, files in os.walk(path3):
        #files=''.join(files)
        
        #print(type(files))
        
        for str1 in files:
                if 'c'==str1.split('.').pop():
                        print("Root = ", root, "dirs = ", dirs, "files = ", str1)
                        count= len(open(root+'\\'+str1,'rU',encoding= 'gbk').readlines())
                        iforc=iforc+int(count)
                        print('行数为:',count)
                if 'cpp'==str1.split('.').pop() and len(str1.split('.'))==2 and root.split('\\').pop()!='proj.wp8' and root.split('\\').pop()!='proj.winrt':
                        print("Root = ", root, "dirs = ", dirs, "files = ", str1)
                        count= len(open(root+'\\'+str1,'rU',encoding= 'gbk').readlines())
                        '''file =  open(root+'\\'+str1, "rb")#要有"rb"，如果没有这个的话，默认使用gbk读文件。           
                        buf = file.read()   
                        result = chardet.detect(buf)   
                        file = open(root+'\\'+str1,"r",encoding=result["encoding"])
                        count=len(file.readlines())'''
                        iforcpp=iforcpp+int(count)
                        print('行数为:',count)

for root, dirs, files in os.walk(path4):
        #files=''.join(files)
        
        #print(type(files))
        for str1 in files:
                if 'java'==str1.split('.').pop()and root.split('\\').pop()!='style':
                        print("Root = ", root, "dirs = ", dirs, "files = ", str1)
                        count= len(open(root+'\\'+str1,'rU',encoding= ('gbk' or 'utf-8')).readlines())
                        iforjava=iforjava+int(count)
                        print('行数为:',count)

i=iforjava+iforc+iforcpp                       
print('总行数为:',i)
lineall=str(i)

g.msgbox("嗨，你一共写了"+lineall+"行代码，要继续加油哦^_^")
g.msgbox("其中\nC语言"+str(iforc)+"行\nC++"+str(iforcpp)+"行\njava"+str(iforjava)+"行")

os.system('pause')
