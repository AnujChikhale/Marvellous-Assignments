from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

def testing_model(test_data):
    Data = [
        {'Studyhours':2, 'Attendance':60, 'Result': 'Fail'},
        {'Studyhours':5, 'Attendance':80, 'Result': 'Pass'},
        {'Studyhours':6, 'Attendance':85, 'Result': 'Pass'},
        {'Studyhours':1, 'Attendance':50, 'Result': 'Fail'}
    ]
    df = pd.DataFrame(Data)
    
    X = df.drop('Result', axis=1)
    Y = df['Result']

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3, random_state=42)

    model = KNeighborsClassifier(n_neighbors=1)

    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(test_data)

    print("Prediction is: ",Y_pred)

def main():

    Studyhours = int(input("Enter the study hours: "))
    Attendance = int(input("Enter the Attendance: "))
    test_data = [[Studyhours,Attendance]]

    testing_model(test_data)

if __name__ == "__main__":
    main()