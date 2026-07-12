import multiprocessing

def Prime(a):
    count = 0
    for i in range(2, a + 1):
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    print(f"Prime numbers count in {a} is", count)

def main():
    Data = [1000,2000,3000,4000]

    pobj = multiprocessing.Pool()
    result = pobj.map(Prime, Data)
    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()
    



