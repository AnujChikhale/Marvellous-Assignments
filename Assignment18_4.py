def Frequency(list, number):
    freq = 0
    for i in range(0,len(list)):      
        if(list[i] == number):
            freq = freq+1
    return freq

def main():
    N = int(input("Enter the Number of elements: "))
    a = []
    for i in range(N):
        x = int(input(f"Enter element {i+1}: "))
        a.append(x)
    No = int(input("Enter the number to search: "))
    print("Addition of elements is: ",Frequency(a, No))

if __name__ == "__main__":
    main()