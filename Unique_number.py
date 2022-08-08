n=int(input())
p=n
f=str(n)
s=set(f)
if len(f)==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")