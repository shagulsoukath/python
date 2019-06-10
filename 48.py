s=int(input())
a=input()
a=a.split()
e=0
a=list(map(int,a))
for i in a:
    e=e+i
    d=e//s
print(d)
