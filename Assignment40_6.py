import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
    model = DecisionTreeClassifier()
    model = model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    accuracy_sklearn = accuracy_score(Y_test,Y_pred)

    Sum = 0
    for actual, predicted in zip(Y_test,Y_pred):
        if(actual != predicted):
            print("Actual: ",actual, "Predicted: ",predicted)
            Sum = Sum+1
    print("Number of Misclassified students is: ",Sum)


if __name__ == "__main__":
    main()