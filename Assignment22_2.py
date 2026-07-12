import multiprocessing
import os

def FactoriaL(a):
    print("Process is running with PID: ",os.getpid())
    Fact = 1
    for i in range(1,a+1):
        Fact = Fact*i
    print(f"Factorial of {a} is: ",Fact)

def main():
    Data = [10,15,20,25]
    result = []

    pobj = multiprocessing.Pool()
    result = pobj.map(FactoriaL, Data)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()