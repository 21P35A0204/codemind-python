n=int(input())
lst=list(map(int,input().split()))
ele=int(input())
cnt=0
for i in lst:
    if i==ele:
        cnt+=1
print(cnt)
        