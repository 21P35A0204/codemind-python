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
print(sum(p)-sum(l))