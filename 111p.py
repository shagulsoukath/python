d=input().split()
f=input().split()
a=int(d[0])
b=int(d[1])
c=f[:a]
e=f[a:]
s=[]
for i in range(len(c)):
    if c[i] in e:
        s.append(c[i])
s.sort()
r=list(dict.fromkeys(s))
print(*r,sep=' ')
        
