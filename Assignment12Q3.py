def Calculator(a, b):
    print("Addition is: ", a+b)
    print("Subtraction is: ", a-b)
    print("Mutiplication is: ", a*b)
    print("Division is: ", a/b)

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    Calculator(a,b)

if __name__ == "__main__":
    main()
