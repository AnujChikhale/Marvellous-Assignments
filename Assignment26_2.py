class Circle:
    PI = 3.14
    def __init__(self):
        self.radius = 0
        self.area = 0
        self.circumference = 0
    def Accept(self):
        self.radius = int(input("Enter the radius of the circle: "))

    def CalculateArea(self):
        self.area = self.PI*self.radius**2

    def CalculateCircumference(self):
        self.circumference = 2*self.PI*self.radius

    def Display(self):
        print("Radius: ",self.radius)
        print("Area",self.area)
        print("Circumference",self.circumference)


dobj = Circle()
dobj.Accept()
dobj.CalculateArea()
dobj.CalculateCircumference()
dobj.Display()
