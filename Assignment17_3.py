def Factorial(a):
    Fact = 1
    for i in range(1,a+1):
        Fact = Fact*i
    return Fact

def main():
    a = int(input("Enter number: "))
    print(f"Factorial of {a} is: ",Factorial(a))

if __name__ == "__main__":
    main()
