n=int(input())
l=list(int(i) for i in input().split())
a=[]
for i in l:
    if l.count(i)==i:
        a.append(i)
#f=max(a)
#g=min(a)
if len(a)>0:
    print(min(a),max(a))
else:
    print(-1)
    
