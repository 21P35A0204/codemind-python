n=int(input())
lst=list(map(int,input().split()))
g=[]
for i in lst:
    if i%2==1:
        g.append(i)
print(g[-1])
        