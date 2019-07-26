aa=input().split()
b=int(aa[1])
c=input().split()
l=[]
for i in c:
    l.append(i)
l.sort()
a=l[::-1]
print(a[b-1])
