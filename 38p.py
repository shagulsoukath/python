a=int(input())
l=[]
l2=[]
for i in range(1,a+1):
	if(a%i==0):
		l.append(i)

for j in l:
	if(j%2==0):
		l2.append(j)
print(*l2,sep=' ')
