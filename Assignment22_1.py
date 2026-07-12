import multiprocessing

def SumSquare(a):
    Sum = 0
    for i in range(1,a+1):
        Sum = Sum + i*i
    return Sum

def main():
    Data = [100000,200000,300000,400000,500000]
    result = []
    pobj = multiprocessing.Pool()
    result = pobj.map(SumSquare,Data)
    pobj.close()
    pobj.join()
    print("Result is: ",result)

if __name__ == "__main__":
    main()