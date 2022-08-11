n=int(input())
m=int(input())
v=[]
t=[]
for i in range(1,n):
    if n%i==0:
        v.append(i)
for j in range(1,m):
    if m%j==0:
        t.append(j)
if n==sum(t) and m==sum(v):
    print("Amicable")
else:
    print("Not Amicable")