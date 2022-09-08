n=int(input())
l=[int(i) for i in input().split()]
p=min(l)
d=[]
for i in l:
    if len(str(i))==len(str(p)):
        d.append(i)
print(len(d))