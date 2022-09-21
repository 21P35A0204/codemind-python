n,m=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
for i in a:
    if i not in b:
        print(i,end=' ')
for j in b:
    if j not in a:
        print(j,end=' ')
