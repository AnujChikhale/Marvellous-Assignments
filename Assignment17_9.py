def NumberOfDigit(a):
    return len(a) 

def main():
    a= input("Enter the digit: ")
    print(f"Number of digits in {a} is: ",NumberOfDigit(a))

if __name__ == "__main__":
    main()