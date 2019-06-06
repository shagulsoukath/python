n=int(input())
s=input()
s=s.split()
s=list(map(int,s))
for i in range(0,len(s)):
    print(s[i],' ',i)
    print("\n")

