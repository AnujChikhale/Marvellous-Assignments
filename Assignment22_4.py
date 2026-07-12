import multiprocessing
import time

def PowerOf5(a):
    Sum = 0
    for i in range(1,a+1):
        Sum = Sum + i**5
    return Sum

def main():
    Data = [10000000,20000000,30000000,40000000,50000000]

    start_time = time.perf_counter()
    result = []
    pobj = multiprocessing.Pool()
    result = pobj.map(PowerOf5,Data)
    end_time = time.perf_counter()

    print("Result is: ", result)
    print("Time required for execution: ", end_time-start_time)

if __name__ == "__main__":
    main()

