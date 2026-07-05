from PersonalLibrary import filterA

Strgt5 = lambda x : len(x) > 5

def main():
    strings = []
    no = int(input("Enter number of strings: "))
    for i in range(0,no):
        str = input("Enter the string: ")
        strings.append(str)

    ret = list(filterA(Strgt5, strings))
    print(ret)

if __name__ == "__main__":
    main()