def NaturalNumbersSums():
    a = int(input("Enter the number: "))
    fact = 1
    for i in range (1 , a+1):
        fact = fact*i
    return fact

def main():
    print(NaturalNumbersSums())

if __name__ == "__main__":
    main()