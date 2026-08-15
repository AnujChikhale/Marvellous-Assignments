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
    train_accuracy = accuracy_score(Y_train, Y_pred)
    test_accuracy = accuracy_score(Y_test, Y_pred)
    print("Train Accuracy is: ",train_accuracy)
    print("Test Accuracy is: ",test_accuracy)

    #The model is underfitted because the Train accuracy is less than test accuracy
    
    

if __name__ == "__main__":
    main()