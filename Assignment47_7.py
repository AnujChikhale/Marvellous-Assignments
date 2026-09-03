import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def main():

    data = {
        'StudyHours': [1,2,3,4,5],
        'Marks': [50,55,60,65,70]
    }
    df = pd.DataFrame(data)

    X = df[['StudyHours']]
    Y = df[['Marks']]
    print(X,Y)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = LinearRegression()
    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print(mean_squared_error(Y_pred,Y_test))
    print(model.coef_)
    print(model.intercept_)


if __name__ == "__main__":
    main()