n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i%2==0:
        k.append(i)
if len(l)==len(k):
    print(True)
else:
    print(False)