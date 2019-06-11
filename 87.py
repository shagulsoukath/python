g=input()
g=g.split()
a=int(g[0])
b=int(g[1])
l=[]
if(b==0):
    print(a)
else:
    print(b)
for i in range(a,b+1):
    if((a%i==0) and (b%i==0)):
        l.apprnd(i)
    print(l)
    
