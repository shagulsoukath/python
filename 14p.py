d=int(input())
f=input()
f=list(f)
o=[]
for i in f:
    if(i!='a' and i!='e' and i!='i' and i!='0' and i!='u'):
        o.append(i)
h=o[::-1]
print(*h,sep='')
