n=int(input())
l=[int(i) for i in input().split()]
k=[str(i) for i in l]
h=max(k)
x=0
for i in k:
    if len(i)==len(h):
        x+=1
print(x)