import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    df = pd.read_csv("student_performance_ml.csv")
    df["Performance_index"] = (df["StudyHours"]*2)+df["Attendance"]
    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=0)
    model = DecisionTreeClassifier(max_depth=None)

    model.fit(X_train, Y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_accuracy = accuracy_score(Y_train, train_pred)
    test_accuracy = accuracy_score(Y_test, test_pred)

    print("Training Accuracy:", train_accuracy)
    print("Testing Accuracy:", test_accuracy)

    #Both the accuracies are same

if __name__ == "__main__":
    main()