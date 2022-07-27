n=int(input())
rev=0
p=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if p==rev:
    print(True)
else:
    print(False)