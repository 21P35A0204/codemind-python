for _ in range(int(input())):
    dnum = int(input())

    bnum = 0
    mul = 1
    while dnum>0:
        rem = dnum%2
        bnum = bnum+(rem*mul)
        mul = mul*10
        dnum = int(dnum/2)
    
    print(bnum)