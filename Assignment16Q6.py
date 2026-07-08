def ChkNumber(a):
    if(a>0):
        print("Positive number")
    elif(a<0):
        print("Negative number")
    else:
        print("Zero")

def main():
    a = int(input("Enter Number: "))
    ChkNumber(a)

if __name__ == "__main__":
    main()