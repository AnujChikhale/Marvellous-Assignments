from PersonalLibrary import MaxOf2, MinOf2

MaxNumber = lambda x,y : MaxOf2(x,y)
MinNumber = lambda x,y : MinOf2(x,y)

def main():
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    print("Max number is: ",MaxNumber(x,y))
    print("Min number is: ",MinNumber(x,y))

if __name__ == "__main__":
    main()