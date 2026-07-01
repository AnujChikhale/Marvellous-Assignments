def CircleArea(r):
    pi = 3.14
    print("Area of circle is: ", pi*r*r)

def main():
    radius = int(input("Enter the radius of circle: "))
    CircleArea(radius)

if __name__ == "__main__":
    main()