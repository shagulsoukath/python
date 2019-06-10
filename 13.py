u=int(input())
if(u>1):
    for i in range(2,u//2):
        if(u%i)==0:
            print("no")
            break
    else:
        print("yes")
