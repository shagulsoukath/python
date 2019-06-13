k=int(input())
for i in range(2,k):
    if(k%i==0):
        print("yes")
        break
else:
    print("no")
