from PersonalLibrary import filterA

DivisibleBy3and5 = lambda x : x%3==0 and x%5==0

def main():
    data = [3,6,9,12,15,20,23,60]
    ret = list(filterA(DivisibleBy3and5, data))
    print(ret)

if __name__ == "__main__":
    main()