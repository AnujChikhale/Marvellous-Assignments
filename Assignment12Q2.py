def Factor(a):
    for i in range(1,a+1):
        if(a%i == 0):
            print(i)
    

def main():
    a = int(input("Enter the number: "))
    Factor(a)

if __name__ == "__main__":
    main()

