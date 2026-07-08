def DivisibleBy5(a):
    if(a%5==0):
        return True
    else:
        return False
    
def main():
    a = int(input("Enter number: "))
    print(DivisibleBy5(a))

if __name__ == "__main__":
    main()