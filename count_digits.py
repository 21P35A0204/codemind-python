n=int(input())
l=[int(i) for i in input().split()]
def lent(g):
    n=abs(g)
    c=0
    if n==0:
        return 1
    while n>0:
        r=n%10
        c+=1
        n=n//10
    return c
d=[]
for j in l:
    d.append(lent(j))
print(*d)
    