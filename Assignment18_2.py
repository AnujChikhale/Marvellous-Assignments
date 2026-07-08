def MaxElement(a):
    Max = 0
    for i in range(len(a)):
        if(a[i]>Max):
            Max = a[i]
    return Max

def main():
    N = int(input("Enter the Number of elements: "))
    a = []
    for i in range(N):
        x = int(input(f"Enter element {i+1}: "))
        a.append(x)
    print("Maximum number is: ",MaxElement(a))

if __name__ == "__main__":
    main()