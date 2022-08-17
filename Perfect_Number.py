def perft(n):
    c=0
    if n>0:
        for i in range(1,n-1):
            if n%i==0:
                c+=i
        if c==n:
            return True
        else:
            return False
    else:
        print(False)
n=int(input())
g=perft(n)
print(g)
                