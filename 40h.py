g=input()
g=list(map(int,g))
s=0
for i in g:
    s=s+int(i)
if(str(s)==str(s)[::-1]):
    print("yes")
else:
    print("no")
