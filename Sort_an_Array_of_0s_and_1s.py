h=[]
f=[]
n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i==0:
        h.append(i)
    else:
        f.append(i)
s=(h+f)
print(*s)