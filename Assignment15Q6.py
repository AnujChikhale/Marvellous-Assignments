from PersonalLibrary import MinOf2
from functools import reduce

Minimum = lambda x,y : MinOf2(x,y)

def main():
    Data = [23,35,12,2,23,4]

    ret = reduce(Minimum, Data)
    print(ret)

if __name__ == "__main__":
    main()