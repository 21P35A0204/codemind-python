n=int(input())
l=[int(i) for i in input().split()]
d=[]
f=[]
g=[]
for i in range(n):
    if i%2==0:
        d.append(l[i])
    else:
        f.append(l[i])
s=0
for i in f:
    for j in range(i):
        g.append(d[s])
    s+=1
print(*g)