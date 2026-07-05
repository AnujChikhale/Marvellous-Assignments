from functools import reduce

Addition = lambda no1, no2 : no1+no2 

def main():
    Data = [1,2,3,4,5,6]

    ret = reduce(Addition, Data)    #remember never to use "list(reduce(Addition, Data))" because reduce returns only single value so no need to write list

    print(ret)

if __name__ == "__main__":
    main()