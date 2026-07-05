from PersonalLibrary import filterA

OddNumber = lambda No : (No % 2 != 0)

def main():
    Data = [3,5,2,3,6,8,75,24]
    FData = list(filterA(OddNumber, Data))
    print("Data after filter: ", FData)

if __name__ == "__main__":
    main()
