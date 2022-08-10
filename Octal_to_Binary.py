for _ in range(int(input())):
    def OctToBin(o):
        return bin(int(o, 8))
    onum = input()
    
    bnum = OctToBin(onum)
    print(bnum[2:])