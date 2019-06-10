g=int(input())
for i in range(2,g//2):
    if(g%i)==0:
        print("yes")
        break
    else:
        print("no")
