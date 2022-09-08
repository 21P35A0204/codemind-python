s=input()
O="aeiouAEIOU"
j=s.split()
b=0
for i in j:
    if i[0] in O and i[-1] not in O:
        b+=1
print(b)

