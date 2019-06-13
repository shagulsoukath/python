g=input()
g=g.split()
a=int(g[1])
h=input()
h=h.split()
h=list(map(int,h))
c=0
for i in h:
    if(i==a):
        c=c+1
if(c>0):
    print("Yes")
else:
    print("No")

