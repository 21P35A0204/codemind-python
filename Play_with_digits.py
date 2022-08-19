def rev(n):
    h=n
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return s
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if rev(i)>0:
        k.append(rev(i))
print(sum(k))