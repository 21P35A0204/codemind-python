n,m=map(int,input().split())
l=[int(i) for i in input().split()]
k=[int(i) for i in input().split()]
d=[]
for i in l:
    if i in k and i not in d:
        d.append(i)
print(*d)