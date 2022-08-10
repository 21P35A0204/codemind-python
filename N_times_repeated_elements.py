n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
for i in l:
    if l.count(i)==k:
        a.append(i)
g=set(a)
if len(g)>0:
    print(*g)
else:
    print(-1)
        
