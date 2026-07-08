def DigitAddition(a):
    Addition = 0
    while(a>0):
        x = a%10
        Addition = Addition + x
        a=a//10
    return Addition 

def main():
    a = int(input("Enter the number: "))

    print(DigitAddition(a))

if __name__ == "__main__":
    main()