class Number:
    Fact = []
    def __init__(self):
        self.Value = int(input("Enter the value: "))

    def chkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True
    
    def chkPerfect(self):
        if(self.Value%1 == 0):
            return True
        else:
            return False
        
    def Factors(self):
        for i in range(1,self.Value):
            if(self.Value%i == 0):
                Number.Fact.append(i)
        print("Sum of Factors are: ",Number.Fact)

    def SumFactor(self):
        Sum = 0
        for no in Number.Fact:
            Sum = Sum + no

        print("Factor is: ",Sum)

nobj = Number()
if(nobj.chkPrime() == True):
    print("Number is Prime")
else:
    print("Number is not prime")
if(nobj.chkPerfect() == True):
    print("Number is Perfect")
else:
    print("Number is not Perfect")
nobj.Factors()
nobj.SumFactor()


        

