import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv('MarvellousInfosystems_PlayPredictor.csv')

    df["Wether"] = df["Wether"].map({
        "Sunny": 0,
        "Overcast": 1,
        "Rainy": 2
    })

    df["Temperature"] = df["Temperature"].map({
        "Hot": 0,
        "Mild": 1,
        "Cool": 2
    })

    df["Play"] = df["Play"].map({
        "No": 0,
        "Yes": 1
    })

    X = df.drop('Play', axis=1)
    Y = df['Play']

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

    model = KNeighborsClassifier(n_neighbors=11)
    model = model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy is: ", accuracy)

    

if __name__ == "__main__":
    main()