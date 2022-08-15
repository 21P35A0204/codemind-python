n=int(input())
l=list(map(int,input().split()))
k=int(input())
d=[]
for i in l:
    if i<=k:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            d.append(i)
print(len(d))
