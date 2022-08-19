def palin(n):
    d=n
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==d:
        return True
g=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if palin(i)==True:
        c+=1
print(c)