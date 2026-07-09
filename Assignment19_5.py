from functools import reduce

def filterFunction(a):
    count = 0
    for i in range(1,a):
        if(a%i==0):
            count = count+1
        if(count <=  1):
            return a

mapFunction  = lambda a : a*2

reduceFunction = lambda a,b: max(a,b)

def main():
    iterable = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        x = int(input(f"Enter number {i+1}: "))

        iterable.append(x)
    print("Original list: ", iterable)
    Fdata = list(filter(filterFunction,iterable))
    Mdata = list(map(mapFunction, Fdata))
    Rdata = reduce(reduceFunction, Mdata)
    print("Filter data: ", Fdata)
    print("Map Data: ", Mdata)
    print("Reduce Data: ", Rdata)

if __name__ == "__main__":
    main()