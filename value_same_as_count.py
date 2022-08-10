n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if l.count(i)==i:
        a.append(i)
f=set(a)
print(len(f))
