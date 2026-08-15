import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop("FinalResult",axis=1)
    Y = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model1 = DecisionTreeClassifier(max_depth=1)
    
    model1 = model1.fit(X_train, Y_train)
    Y_pred1 = model1.predict(X_test)
    test_accuracy = accuracy_score(Y_test, Y_pred1)
    print("Accuracy is of tree with dept=1 is: ",test_accuracy)
    
    model2 = DecisionTreeClassifier(max_depth=2)
    
    model2 = model2.fit(X_train, Y_train)
    Y_pred2 = model2.predict(X_test)
    test_accuracy = accuracy_score(Y_test, Y_pred2)
    print("Accuracy is of tree with dept=2 is: ",test_accuracy)
    
    model3 = DecisionTreeClassifier(max_depth=None)
    
    model3 = model3.fit(X_train, Y_train)
    Y_pred3 = model3.predict(X_test)
    test_accuracy = accuracy_score(Y_test, Y_pred3)
    print("Accuracy is of tree with dept=none is: ",test_accuracy)
    
    

if __name__ == "__main__":
    main()