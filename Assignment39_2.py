import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df.drop("FinalResult",axis=1)
    Y = df["FinalResult"]

    model = DecisionTreeClassifier()
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)
    model = model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    print("Actual values are: ",Y_test)
    print("Predicted values are: ",Y_pred)
    

if __name__ == "__main__":
    main()