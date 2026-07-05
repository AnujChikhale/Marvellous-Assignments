from functools import reduce
from PersonalLibrary import MaxOf2

MaxNumber = lambda x,y : MaxOf2(x,y)

def main():
    Data = [23,53,12,546,23,]

    ret = reduce(MaxNumber, Data)
    print(ret)

if __name__ == "__main__":
    main()