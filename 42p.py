g=int(input())
k=list(map(int,input().split()))
t=list(k)
k.sort()
if k==t:
    print('yes')
else:
    print('no')
