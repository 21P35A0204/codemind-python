n,k=map(int,input().split())
l=[int(i) for i in input().split()]
f=[str(abs(i)) for i in l]
p=0
for i in f:
    if len(i)==k:
        p=p+1
print(p)

        
