n=int(input())
a=n
s=0
if(n>0):
    n=n%10
    s=s+n*n*n
    n=n/10
if(a==s):
    print("yes")
else:
    print("no")
