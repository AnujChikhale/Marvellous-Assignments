def GradeAsPerMarks(a):
    if(a>=75 and a<=100):
        print("Distinction")
    elif(a>=60 and a<75):
        print("First Class")
    elif(a>=50 and a<60):
        print("Second Class")
    elif(a<50 and a>=0):
        print("Fail")
    else:
        print("Invalid Marks")
    
def main():
    marks = int(input("Enter marks: "))
    GradeAsPerMarks(marks)

if __name__ == "__main__":
    main()