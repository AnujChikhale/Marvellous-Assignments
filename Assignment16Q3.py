def Add(a,b):
    return a+b

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    ans = Add(a,b)
    print("Addition of two number is: ",ans)

if __name__ == "__main__":
    main()