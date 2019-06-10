g=input()
l=list(map(int,g))
for i in l:
    if(i==1 or i==0):
       c=1
    else:
        c=0
        
if(c==1):
    print("yes")
else:
    print("no")
