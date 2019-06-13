d=int(input())
f=input()
f=list(f)
l=[]
for i in f:
    if(i!='a' and i!='e' and i!='i' and i!='0' and i!='u'):
        l.append(i)
h=l[::-1]
print(*h,sep='')
