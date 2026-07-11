import threading

def Ascending():
    A = []
    print("Numbers from 1-50 are:")
    for i in range(1,51):
        A.append(i)
    print(A)

def Descending():
    print("Numbers from 50-1 are: ")
    B = []
    i = 50
    while(i>0):
        B.append(i)
        i = i-1
    print(B)

def main():
    Thread1 = threading.Thread(target = Ascending)
    Thread2 = threading.Thread(target = Descending)
    Thread1.start()
    Thread1.join()
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()
