import threading

def Evendigits():
    count = 0
    EvenNumber = []
    for i in range(2,100,2):
        if(count<10):
            EvenNumber.append(i)
            count = count+1
    print(EvenNumber)

def Odddigits():
    count = 0
    OddNumber = []
    for i in range(1,100,2):
        if(count<10):
            OddNumber.append(i)
            count = count+1
    print(OddNumber)

def main():
    Even = threading.Thread(target = Evendigits)
    Odd = threading.Thread(target = Odddigits)
    Even.start()
    Odd.start()
    

if __name__ == "__main__":
    main()