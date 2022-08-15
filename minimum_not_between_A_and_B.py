n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
t=[]
for i in l:
    if i<a or i>b:
        t.append(i)
if len(t)>0:
    print(min(t))
else:
    print(-1)
    