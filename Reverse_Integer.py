n=int(input())
f=n
s=0
if n<0:
    n=n*(-1)
while n:
    r=n%10
    s=s*10+r
    n=n//10
if f<0:
    print(-s)
else:
    print(s)
    
    