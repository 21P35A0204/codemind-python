n=int(input())
l=[int(i) for i in input().split()]
s=0
for i in range(1,n-1):
    if l[(i-1)]%2==0 and l[(i+1)]%2!=0 or l[(i-1)]%2!=0 and l[(i+1)]%2==0:
        s+=1
print(s)