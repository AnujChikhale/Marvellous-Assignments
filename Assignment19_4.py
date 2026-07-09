from functools import reduce

filterFunction = lambda a : a%2==0

mapFunction  = lambda a : a*a

reduceFunction = lambda a,b: a+b

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