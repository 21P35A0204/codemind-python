n=int(input())
l=[int(i) for i in input().split()]
d=[]
f=[]
g=[]
for i in range(n):
    if i%2==0:
        d.append(l[i])
    else:
        g.append(l[i])
s=0    
for i in g:
    for j in range(i):
        f.append(d[s])
    s+=1
print(*f)
    