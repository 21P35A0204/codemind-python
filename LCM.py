a,b=map(int,input().split())
k=[]
l=[]
f=max(a,b)
for i in range(1,f+1):
    g=a*i
    h=b*i
    k.append(g)
    l.append(h)
for i in l:
    if i in k:
        print(i)
        break
        
    
    