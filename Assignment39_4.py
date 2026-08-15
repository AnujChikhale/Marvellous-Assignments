import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop("FinalResult",axis=1)
    Y = df["FinalResult"]

    model = DecisionTreeClassifier()
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)
    model = model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy is : ", accuracy)
    ConfusionMatrixDisplay = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix is: ",ConfusionMatrixDisplay)
    print("True Positive: ", ConfusionMatrixDisplay[0][0])
    print("False negative: ", ConfusionMatrixDisplay[0][1])
    print("False Positive: ", ConfusionMatrixDisplay[1][0])
    print("True Negative: ", ConfusionMatrixDisplay[1][1])
    

if __name__ == "__main__":
    main()