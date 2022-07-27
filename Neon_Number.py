n=int(input())
k=n
p=n**2
sum=0
while p>0:
    r=p%10
    sum=sum+r
    p=p//10
if sum==k:
    print("Neon Number")
else:
    print("Not Neon Number")
