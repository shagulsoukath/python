n=int(input())
l=[]
for i in range(1,n+1):
    n=n*i
    l.append(str(n))
a=" ".join(l)
print(a)
