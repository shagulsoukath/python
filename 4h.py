op=int(input())
s=input().split()
l=[]
l2=[]
l3=[]
l4=[]
for i in s:
    l.append(i)
for j in l:
    if j not in l2:
        l2.append(j)
    else:
        l3.append(j)
for k in l2:
  if k not in l3:
      l4.append(k)
print(*l4,sep=' ')
