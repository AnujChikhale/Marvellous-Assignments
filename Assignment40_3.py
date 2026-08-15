import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    model = DecisionTreeClassifier()
    model = model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    accuracy_initial = accuracy_score(Y_test,Y_pred)

    df = df.drop("SleepHours", axis=1)
    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
    model = DecisionTreeClassifier()
    model1 = model.fit(X_train,Y_train)
    Y_pred1 = model.predict(X_test)
    accuracy1 = accuracy_score(Y_test,Y_pred1)
    print(accuracy1)

    X1 = df[["StudyHours", "Attendance"]]
    Y1 = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X1,Y1,test_size=0.5,random_state=42)
    model2 = DecisionTreeClassifier()
    model2 = model.fit(X_train,Y_train)
    Y_pred2 = model.predict(X_test)
    accuracy2 = accuracy_score(Y_test,Y_pred2)
    print(accuracy2)


    #Accuracy is same in both the case
    

if __name__ == "__main__":
    main()