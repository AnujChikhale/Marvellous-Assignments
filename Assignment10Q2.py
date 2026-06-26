def NaturalNumbersSums():
    a = int(input("Enter the number: "))
    sum = 0
    for i in range (a+1):
        sum = sum + i
    return sum

def main():
    print(NaturalNumbersSums())

if __name__ == "__main__":
    main()