import threading

def Factor_even(a):
    Even_factors = []
    Sum = 0
    for i in range(1,a):
        if(a%i == 0 and i%2==0):
            Even_factors.append(i)
    for no in Even_factors:
        Sum = Sum+no

    print(f"Sum of Even factors of {a} is: ", Sum)

def Factor_odd(a):
    Odd_factors = []
    Sum = 0
    for i in range(1,a):
        if(a%i == 0 and i%2!=0):
            Odd_factors.append(i)
    for no in Odd_factors:
        Sum = Sum+no

    print(f"Sum of Odd factors of {a} is: ", Sum)


def main():
    a = 20
    EvenFactor = threading.Thread(target = Factor_even, args=(a,))
    OddFactor = threading.Thread(target = Factor_odd, args=(a,))
    EvenFactor.start()
    OddFactor.start()
    EvenFactor.join()
    OddFactor.join()
    print("Exit from main")

if __name__ == "__main__":
    main()

