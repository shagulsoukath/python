l=int(input())
a=list(str(l))
s=0
for i in a:
    s=s+int(i)
if(s%2==0):
    print("E")
else:
    print("O")
