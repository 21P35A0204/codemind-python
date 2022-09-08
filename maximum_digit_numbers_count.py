n=int(input())
l=[int(i) for i in input().split()]
a=[str(i) for i in l]
j=[len(i) for i in a]
k=max(j)
for i in range(n):
    if j[i]>=k:
        print(l[i],end=' ')