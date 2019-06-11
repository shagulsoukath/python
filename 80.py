d=input()
l=[]
for i in d:
    if(int(i)%2!=0):
        l.append(i)
print(*l,sep=' ')

