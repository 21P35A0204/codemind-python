s=map(str,input().split())
j=[]
g=[]
for i in s:
    j.append(max(i))
    g.append(min(i))
p=[]
l=[]
for i in j:
    p.append(ord(i))
for i in g:
    l.append(ord(i))
c=0
d=0
a=[]
for i in range(len(p)):
    a.append(abs(p[c]-l[d]))
    c+=1
    d+=1
print(*a)
    