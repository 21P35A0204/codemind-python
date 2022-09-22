n=int(input())
l=list(map(int,input().split()))
l.reverse()
for i in range(n):
    if l[i]%2!=0:
        print(abs(n-1)-i)
        break

        