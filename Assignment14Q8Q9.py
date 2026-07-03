Addition = lambda a,b : a+b
Multiplication = lambda a,b : a*b

def main():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    print("Addition of number is: ",Addition(a,b))
    print("Multiplication of number is: ",Multiplication(a,b))

if __name__ == "__main__":
    main()