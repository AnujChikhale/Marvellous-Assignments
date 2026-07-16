class Arithematic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter value1: "))
        self.Value2 = int(input("Enter value2: "))

    def Addition(self):
        print(self.Value1+self.Value2)
    
    def Subtraction(self):
        print(self.Value1-self.Value2)
    
    def Multiplication(self):
        print(self.Value1*self.Value2)
    
    def Division(self):
        try:
            print(self.Value1/self.Value2)
        except ZeroDivisionError:
            print("Zero division error")


aobj = Arithematic()
aobj.Accept()
aobj.Addition()
aobj.Subtraction()
aobj.Multiplication()
aobj.Division()