h=input()
h=h.split(" ")
g=[]
for i in h:
    g.append(i[::-1])
print(*g,sep=' ')
