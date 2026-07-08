from PersonalLibrary import ChkPrime

def ListPrime(a):
    list = []
    Sum = 0
    for no in a:
        if(ChkPrime(no) == True):
            list.append(no)
    for no in list:
        Sum = Sum + no
    return Sum
    
def main():
    N = int(input("Enter number of elements: "))
    a = []
    for i in range(N):
        P = int(input(f"Enter number {i+1}: "))
        a.append(P)
    print("Sum of prime numbers is: ",ListPrime(a))

if __name__ == "__main__":
    main()