n=int(input())
l=[int(i) for i in input().split()]
k=sum(l)//n
if k in l:
    print(True)
else:
    print(False)