n=int(input())
g=n
l=len(str(n))
s=0
while n>0:
    r=n%10
    s+=r**l
    n=n//10
    l-=1
if g==s:
    print(True)
else:
    print(False)
