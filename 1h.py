a=int(input())
s=input().split()
l=[]
l2=[]
l3=[]
for i in s:
    l.append(i)
for j in l:
    if j not in l2:
        l2.append(j)
    else:
        l3.append(j)
d=set(l3)
g=list(d)
g.sort()
if(len(g)==0):
    print("unique")
else:
    print(*g,sep=' ')

