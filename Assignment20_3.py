import threading

def Even(*a):
    Sum_even = 0
    print("Values in a are: ",a)
    List_even = []
    for no in a:
        if(no%2 == 0):
            List_even.append(no)
    print("Even vlaues are: ",List_even)
    for no in List_even:
        Sum_even = Sum_even+no
    print("Sum of Even values = ", Sum_even)

def Odd(*a):
    Sum_odd = 0
    print("Values in a are: ",a)
    List_odd = []
    for no in a:
        if(no%2 != 0):
            List_odd.append(no)
    print("Odd values are: ",List_odd)
    for no in List_odd:
        Sum_odd = Sum_odd+no
    print("Sum of Even values = ", Sum_odd)

def main():
    EvenList = threading.Thread(target=Even, args=(1,2,3,4,5,6,7,8,9,10,))
    OddList = threading.Thread(target=Odd, args=(1,2,3,4,5,6,7,8,9,10,))
    EvenList.start()
    OddList.start()
    EvenList.join()
    OddList.join()
    print("End of main")

if __name__ == "__main__":
    main()