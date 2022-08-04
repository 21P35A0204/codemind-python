n=int(input())
cnt=[]
bnt=[]
lst=list(map(int,input().split()))
for i in lst:
    if i%2==1:
        cnt.append(i)
    elif i%2==0:
        bnt.append(i)
print(*cnt+bnt)
        
        
        