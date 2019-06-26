s=int(input())
d=input().split()
d=list(map(int,d))
l=[]
l2=[]
for i in d:
    l.append(i)
for j in l:
    if(j<s):
        l2.append(j)
print(*l2,sep=' ')
