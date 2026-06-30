def Prime(a):
    if(a==1 or a==2 or a==3 or a==5 or a==7):
        print("Number is Prime")
    elif(a%2 ==0 or a%3==0 or a%5==0 or a%7==0):
        print("Number is not prime")
    else:
        print("Number is prime")

def main():
    a = int(input("Enter the Number: "))
    Prime(a)

if __name__ == "__main__":
    main()