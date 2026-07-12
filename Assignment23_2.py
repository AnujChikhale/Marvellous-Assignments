import os
import multiprocessing

def SumOdd(a):
    
    Sum = 0
    
    for i in range(1,a,2):
        Sum = Sum + i
    print("Input number: ",a)
    print("Sum of odd numbers: ",Sum)
    print(f"Process ID of {a}: ", os.getpid())

def main():
    Data = [1000000,2000000,3000000,4000000]
    result = []
    pobj = multiprocessing.Pool()
    result = pobj.map(SumOdd,Data)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()