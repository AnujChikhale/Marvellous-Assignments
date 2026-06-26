def divisible(a):
    if(a%3 == 0 and a%5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

def main():
    divisible(10)

if __name__ == "__main__":
    main()