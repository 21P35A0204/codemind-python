n=int(input())
d=[]
c=0
if n==0:
    print("YES")
else:    
    for j in range(2,n+1):
        if n%j==0:
            d.append(j)
    for i in range(len(d)-1):
        if d[i]*d[i+1]==n and abs(d[i]-d[i+1])==1:
            c+=1
if c>=1:
    print("YES")
else:
    print("NO")
        