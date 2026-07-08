def Factor_Addition(a):
    Add = 0
    for i in range(1,a):
        
        if(a%i == 0):
            Add = Add+i
    return Add

def main():
    a = int(input("Enter the number: "))
    ans = Factor_Addition(a)
    print(f"Addition of factors of {a} is: ", ans)

if __name__ == "__main__":
    main()

