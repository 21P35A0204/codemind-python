n=int(input())
lst=list(map(int,input().split()))
g=sum(lst)//n
cnt=0
for i in lst:
    if i>=g:
        cnt+=1
print(cnt)