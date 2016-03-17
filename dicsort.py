import os
s={'a':68,'b':89,'c':64,'d':88,'e':1,'f':101,'g':34342,'h':6,'i':55}
l=list(s)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(s[l[i]]>s[l[j]]):
            a=l[i]
            l[i]=l[j]
            l[j]=a

for i in range(len(l)):
    print(l[i],s[l[i]])
os.system('pause')
