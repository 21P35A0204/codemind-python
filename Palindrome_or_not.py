n=input()
n=n.lower()
t=list(n)
k=0
v=-1
if len(t)>2:
    
    for k in range(len(t)//2):
        if t[k]==t[v]:
            k+=1
            v-=1
        else:
            print(False)
            break
    if k==len(t)//2:
        print(True)
else:
    if t[0]==t[1]:
        print(True)
    else:
        print(False)