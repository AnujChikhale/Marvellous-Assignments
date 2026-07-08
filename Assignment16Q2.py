def ChkNum(a):
    if(a%2 == 0):
        print("Even number")
    else:
        print("Odd number")

def main():
    No = int(input("Enter the number: "))
    ChkNum(No)

if __name__ == "__main__":
    main()