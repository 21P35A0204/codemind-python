n,m=map(int,input().split())
j=[]
k=[]
h=[]
for i in range(1,n+1):
    if n%i==0:
        j.append(i)
for i in range(1,m+1):
    if m%i==0:
        k.append(i)
for i in j:
    for g in k:
        if i==g:
            h.append(g)
print(max(h))
        
