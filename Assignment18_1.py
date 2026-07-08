def AddElement(a):
    addition = 0
    for i in range(len(a)):
        ans = a[i]
        addition = addition + ans

    return addition

def main():
    N = int(input("Enter the Number of elements: "))
    a = []
    for i in range(N):
        x = int(input(f"Enter element {i+1}: "))
        a.append(x)
    print("Addition of elements is: ",AddElement(a))

if __name__ == "__main__":
    main()