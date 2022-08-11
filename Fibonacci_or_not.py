n=int(input())
a,b=0,1
v=[a,b]
for i in range(2,n):
    c=a+b
    v.append(c)
    a=b
    b=c
print(n in v)