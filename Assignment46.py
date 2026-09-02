import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def main():

    df = pd.read_csv('Advertising.csv')
    print(df.isnull().sum())
    df = pd.DataFrame(df)
    print(df.head())

    X = df.drop('sales', axis=1)
    Y = df['sales']
    print(X.head())
    print(Y.head())

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print("Actual: ",Y_test)
    print("Predicted: ",Y_pred)

    print("Mean Squared error: ", mean_squared_error(Y_test,Y_pred))
    print("R2 Score: ", r2_score(Y_test,Y_pred))

if __name__ == "__main__":
    main()