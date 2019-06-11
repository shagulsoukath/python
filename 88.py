g=input()
g=g.split()
g=list(map(int,g))
a=g[0]
b=g[1]
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print(min1)
        break
    min1=min1+1
