a=input().split()
b=int(a[1])
c=input().split()
l=[]
for i in c:
    l.append(int(i))
l.sort()
aa=l[::-1]
print(aa[b-1])

