d=input().split()
a=int(d[0])
b=int(d[1])
l=[]
for i in range(a,b+1):
    if(i%2!=0):
        l.append(i)
print(sum(l))
