from functools import reduce

product = lambda x,y : x*y

def main():
    Data = [3,1,2,]
    ret = reduce(product, Data)
    print(ret)

if __name__ == "__main__":
    main()