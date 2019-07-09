f=int(input())
s=input().split()
l=[]
l2=[]
c=0

for i in s:
    l.append(i)
m=[]
m.append(l[0])
c=int(l[0])
for j in range(0,f-1):
    c=c+int(l[j+1])
    m.append(c)
a=m
d=m[::-1]
j=[]
for i in range(0,f):
    w=int(a[i])+int(d[i])
    j.append(w)
print(*j,sep=' ')
    
    
    

