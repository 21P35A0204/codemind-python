a,b=map(int,input().split())
def add(a,b):
    while b!=0:
        c=a&b
        a=a^b
        b=c<<1
    return a
print(add(a,b))