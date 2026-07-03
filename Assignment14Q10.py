from PersonalLibrary import MaxOf3

GreatestOf3 = lambda a,b,c : MaxOf3(a,b,c)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print(GreatestOf3(a,b,c))

if __name__ == "__main__":
    main()