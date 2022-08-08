n=int(input())
c=0
d=0
l=list(map(int,input().split()))
for i in range(n):
    if l[i]%2==1:
        if i%2==1:
            c+=1
    if l[i]%2==1:
        d+=1
if c==d:
    print(True)
else:
    print(False)