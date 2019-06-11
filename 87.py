g=input()
g=g.split()
a=int(g[0])
b=int(g[1])
i=1
while(i<=a and i<=b):
    if((a%i==0) and (b%i==0)):
        gcd=i
    i=i+1
print(gcd)
    

