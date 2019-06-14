    
f=int(input())
c=0
for i in range(1,f+1):
    b=a//i
    if b%2==1 and f%i==0:
        print(i)
        break
