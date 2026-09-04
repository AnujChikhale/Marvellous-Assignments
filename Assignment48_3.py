import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def main():

    data = {
        'Experience':[1,2,3,4,5],
        'Salary':[20000,25000,30000,35000,40000]
    }

    df = pd.DataFrame(data)
    X = df[['Experience']]
    Y = df[['Salary']]

    X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = LinearRegression()
    model = model.fit(X_train,Y_train)

    Y_pred = model.predict([[6]])
    print("Predicted salary for 6 years experience is: ",Y_pred[0][0])
    

    plt.plot(X,Y, color = 'g', label="Regression Line")
    plt.scatter(X,Y,color='r', label = "Scatter plot")
    plt.xlabel("X: Independent variables")
    plt.ylabel("Y: dependent variables")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()