import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def main():
    data = pd.read_csv('breast_cancer.csv')
    df = pd.DataFrame(data)
    X = df.drop('target', axis=1)
    Y = df['target']
    

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    model = LogisticRegression()
    model = model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("Accuracy: ",accuracy_score(Y_pred,Y_test))
    print("Confusion matrix: ",confusion_matrix(Y_pred,Y_test))
    print("Classification report: ",classification_report(Y_pred,Y_test))


if __name__ == "__main__":
    main()