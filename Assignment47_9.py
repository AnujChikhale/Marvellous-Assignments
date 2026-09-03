import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def main():

    data = {
        'StudyHours': [1,2,3,4,5],
        'SleepHours': [7,6,7,6,8],
        'Marks': [50,55,60,65,70]
    }
    df = pd.DataFrame(data)

    X = df[['StudyHours','SleepHours']]
    Y = df[['Marks']]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = LinearRegression()
    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)
    
    print("Coefficient of StudyHours: ",model.coef_[0][0])
    print("Coefficient of SleepHours: ",model.coef_[0][1])
    print(model.intercept_)



if __name__ == "__main__":
    main()