n=int(input())
cnt=0
for i in range(n):
    if i*i==n:
        cnt+=1
if cnt==1:
    print(True)
else:
    print(False)