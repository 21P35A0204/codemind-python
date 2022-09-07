n=int(input())
l=[int(i) for i in input().split()]
def lent(k):
    d=0
    while k>0:
        r=k%10
        d+=1
        k=k//10
    return d
g=min(l)
c=0
for i in l:
    if lent(i)==lent(g):
        c+=1
print(c)
    