h=int(input())
l=[]
for i in range(1,h+1):
    if(h%i==0):
        l.append(i)
print(*l,sep=' ')
