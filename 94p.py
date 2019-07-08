s=input()
a=len(s)
c=0
for i in range(0,a):
    for j in range(i+1,a):
        if(s[i]==s[j]):
            c=c+1
            break
if(c>=1):
    print("yes")
else:
    print("no")
        
