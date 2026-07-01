def binaryEquivalent(a):
    ans = []
    if(a==0):
        return 0
    while(a>0):
        remainder = a%2
        a = a//2
        print(remainder)
    

binaryEquivalent(7)