l=[]
n=int(input())
c=1
for i in range(n+1):
    if i>0:
        l.append(c/i)
print("{:.2f}".format(sum(l)))