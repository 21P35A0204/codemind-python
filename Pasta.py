a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(len(m)):
    if m[i] in n:
        n.remove(m[i])
    else:
        print("No")
        break
else:
    print("Yes")
        