import numpy as np

def main():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    size = len(X)

    sum_X = 0
    sum_Y = 0

    for i in range(size):
        sum_X=sum_X+X[i]
        sum_Y=sum_Y+Y[i]
    mean_X = sum_X/size
    mean_Y = sum_Y/size

    print("X mean: ",mean_X)
    print("Y mean: ",mean_Y)

    numerator = 0
    denominator = 0

    for i in range(size):
        numerator = numerator + (X[i]-mean_X)*(Y[i]-mean_Y)
        denominator = denominator + (X[i]-mean_X)**2
    slope = numerator/denominator
    print("Slope is : ",slope)

    Y_intercept = mean_Y - slope*mean_X
    print("Intercept is: ",Y_intercept)

    print(f"Regression equation is: Y = {slope}X + {Y_intercept}")

    X1 = 6
    Y1 = slope*X1 + Y_intercept
    print("Value of Y for X=6 is : ",Y1)


if __name__ == "__main__":
    main()