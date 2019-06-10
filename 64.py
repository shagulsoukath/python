f=input()
f=f.split()
f=list(map(int,f))
s=0
for i in f:
    s=s+i
if(s%2==0):
    print("even")
else:
    print("odd")
)
