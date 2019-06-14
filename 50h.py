g=input()
g=g.split()
a=int(g[0])
b=int(g[1])
p=0
if(b>a):
    print("0")
while(a>=b and a>0):
    a=a-b
    p=p+1
print(p)
