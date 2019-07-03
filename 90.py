d=input()
l=[]
for i in d:
    if(i.isdigit()):
        l.append(i)
print(*l,sep='') 
