def RectangleArea(lenght, width):
    print("Area of rectangle is : ", lenght*width)

def main():
    length = int(input("Enter length of Rectangle: "))
    Width = int(input("Enter width of Rectangle: "))

    RectangleArea(length, Width)

if __name__ == "__main__":
    main()