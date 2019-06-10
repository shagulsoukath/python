d=input()
d=d.split()
s=int(d[0])
a=int(d[1])
l=[]
for i in range(s,a+1):
    if i>1:
        for j in range(2,i):
           if(i%j)==0:
                break
        else:
            l.append(i)
print(*l,sep=' ')
                    
