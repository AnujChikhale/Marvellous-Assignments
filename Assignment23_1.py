import os
import multiprocessing

def SumEven(a):
    
    Sum = 0
    print(f"Process ID of {a}: ", os.getpid())
    for i in range(0,a,2):
        Sum = Sum + i
    print("Input number: ",a)
    print("Sum of even numbers: ",Sum)

def main():
    Data = [1000000,2000000,3000000,4000000]
    result = []
    pobj = multiprocessing.Pool()
    result = pobj.map(SumEven,Data)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()