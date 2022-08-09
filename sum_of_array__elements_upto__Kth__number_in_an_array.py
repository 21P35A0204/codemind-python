n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in l:
    if i==k:
        break
    else:
        c=c+i
print(c+k)
    