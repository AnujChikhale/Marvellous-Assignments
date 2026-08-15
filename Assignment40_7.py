import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=0)
    model = DecisionTreeClassifier()
    model = model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    accuracy1 = accuracy_score(Y_test,Y_pred)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=10)
    model = DecisionTreeClassifier()
    model = model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    accuracy2 = accuracy_score(Y_test,Y_pred)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
    model = DecisionTreeClassifier()
    model = model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    accuracy3 = accuracy_score(Y_test,Y_pred)
    print("Accuracy for random_State = 0 is: ",accuracy1)   #accuracy=1
    print("Accuracy for random_State = 10 is: ",accuracy2)  #accuracy=0.93333
    print("Accuracy for random_State = 42 is: ",accuracy3)  #accuracy=0.93333

if __name__ == "__main__":
    main()