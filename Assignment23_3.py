import os
import multiprocessing

def EvenCount(a):
    
    count = 0
    
    for i in range(0,a):
        if(i%2==0):
            count = count+1
    print("Input number: ",a)
    print("count of even numbers: ",count)
    print(f"Process ID of {a}: ", os.getpid())

def main():
    Data = [1000000,2000000,3000000,4000000]
    result = []
    pobj = multiprocessing.Pool()
    result = pobj.map(EvenCount,Data)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()