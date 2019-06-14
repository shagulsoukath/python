g=input().split()
a=int(g[1])
h=input()
h=h.split()
l=[]
l2=[]
for i in h:
    l.append(int(i))
for i in l:
    if(i<a):
       l2.append(i)
l2.sort()
print(*l2,sep=' ')


