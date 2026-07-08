def MinElement(a):
    min = a[0]
    for i in range(1,len(a)):
        
        if(a[i]<min):
            min = a[i]
    return min

def main():
    N = int(input("Enter the Number of elements: "))
    a = []
    for i in range(N):
        x = int(input(f"Enter element {i+1}: "))
        a.append(x)
    print("Addition of elements is: ",MinElement(a))

if __name__ == "__main__":
    main()