from itertools import permutations
def per(s):
    a=[]
    perm=permutations(s)
    for pe in list(perm):
        d=''.join(pe)
        a.append(d)
        l=set(a)
    for k in l:
        print(k)
s=input()
d=s[::-1]
if(s==d):
    print(s)
else:
    per(s)
