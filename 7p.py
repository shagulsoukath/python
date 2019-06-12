g=input()
g=list(g)
l=[]
for i in range(0,len(g)):
    if(i%2==0):
        l.append(g[i+1])
    elif(i%2!=0):
        l.append(g[i-1])
print(*l,sep='')

