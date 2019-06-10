a=input()
a=a.split()
a=list(map(int,a))
m=1
for i in a:
    m=m*i
if(m%2==0):
    print("even")
else:
    print("odd")
    

