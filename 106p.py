f=int(input())
s=input().split()
d=list(dict.fromkeys(s))
print(*d,sep=' ')
