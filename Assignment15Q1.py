from PersonalLibrary import mapA

Square = lambda x : x*x

def main():
    Data = [3,2,5,67,3]
    MData = list(mapA(Square, Data))
    print(MData)

if __name__ == "__main__":
    main()