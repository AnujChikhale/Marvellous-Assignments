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

    ConfusionMatrix = confusion_matrix(Y_test,Y_pred)
    TP = ConfusionMatrix[0][0]
    FN = ConfusionMatrix[0][1]
    FP = ConfusionMatrix[1][0]
    TN = ConfusionMatrix[1][1]

    self_accuracy_score = (TP+TN)/(TP+TN+FP+FN)

    print("Self calculated accuracy is: ",self_accuracy_score)
    print("SKlearn calculated accuracy is: ",accuracy_sklearn)


if __name__ == "__main__":
    main()
