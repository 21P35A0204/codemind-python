l=list(map(int,input().split(',')))
def fact(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=i
    return c 
e=[]
for i in l:
    f=fact(i)
    if f in l:
        e.append(i)
e.sort()
if len(e)!=0:
    print(*e)
else:
    print(-1)
    
    
            
        