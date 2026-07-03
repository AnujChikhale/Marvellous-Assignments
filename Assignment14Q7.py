DivisibleBy5 = lambda x : x%5 == 0

def main():
    value = int(input("Enter vlaue: "))
    ret = DivisibleBy5(value)
    if(ret == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()