import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    # Step1: Get the data
    df = pd.read_csv("WinePredictor.csv")
    print("Before cleaning", df.shape)
    #Step2: Clean the data
    df = df.dropna(axis=1)
    print("After cleaning", df.shape)
    df = df.drop_duplicates()
    print("Duplicate cleaning", df.shape)

    #Step3: Training the model

    X = df.drop("Class",axis=1)
    Y = df["Class"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    model = DecisionTreeClassifier()
    model = model.fit(X_train,Y_train)

    #Step4: Testing the data

    Y_pred = model.predict(X_test)


    #Step5: Calculating accuracy
    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy is: ",accuracy)




if __name__ == "__main__":
    main()