n=int(input())
lst=list(map(int,input().split()))
dxc=[]
xwe=[]
for i in lst:
    if i%2==0:
        dxc.append(i)
    else:
        xwe.append(i)
print(*dxc+xwe)
    