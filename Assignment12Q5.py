def ReverseNumbers(a):
    while(a>0):
        print(a)
        a = a-1

def main():
    a = int(input("Enter the number: "))
    ReverseNumbers(a)

if __name__ == "__main__":
    main()