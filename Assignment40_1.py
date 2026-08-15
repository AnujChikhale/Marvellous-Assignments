import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    model = DecisionTreeClassifier()
    model = model.fit(X_train,Y_train)
    important_features = model.feature_importances_
    print("Important features are: ",important_features)
    

if __name__ == "__main__":
    main()