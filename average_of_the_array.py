n=int(input())
lst=list(map(int,input().split()))
p=sum(lst)/len(lst)
print("{:.2f}".format(p))