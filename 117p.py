a=input()
b=a[::-1]
l=[]
for i in b:
    l.append(i)
print(*l,sep='-')
