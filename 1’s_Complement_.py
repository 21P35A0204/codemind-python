n=bin(int(input()))
s=n[2:]
t=str(s)
e=''
for i in t:
    if i=="1":
        e+='0'
    else:
        e+="1"
g=int(e,2)
print(g)