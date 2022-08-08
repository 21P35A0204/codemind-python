n=int(input())
l=[int(i) for i in input().split()]
k=[]
for i in l:
    if i not in k :
        k.append(i)
print(*k)
    
    
        
        