e=int(input())
if(e>1):
    for i in range(2,e//2):
        if(e%i)==0:
            print("no")
            break
    else:
        print("yes")
