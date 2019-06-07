n=int(input())
l=[]
a=0
b=1
d=1
for i in range(0,n-1):
    c=a+b
    a=b
    b=c
    l.append(str(c))
m=' '.join(l)
print(d,m)
    
