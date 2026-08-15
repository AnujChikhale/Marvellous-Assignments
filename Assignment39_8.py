import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.tree import DecisionTreeClassifier

def main():
    #1.Dataset loading
    df = pd.read_csv("student_performance_ml.csv")

    #2.Data analysis
    print("Dataset Information: ",df.info())
    print("Dataset stats: ",df.describe())
    print("Final relation distribution: ",df["FinalResult"].value_counts())

    #3.Visualization
    plt.scatter(
        df["StudyHours"],
        df["PreviousScore"]
    )
    plt.title("Visualizing student performance")
    plt.legend()
    plt.show()

    #4.Train - Test split
    X = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    #5.Model training
    model = DecisionTreeClassifier()
    model = model.fit(X_train,Y_train)

    #6.Prediction
    Y_pred = model.predict(X_test)

    #7.Accuracy calculation
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy score is: ",accuracy)

    #8.Confusion matrix generation
    ConfusionMatrix = confusion_matrix(Y_test, Y_pred)
    print(ConfusionMatrix)

    #9.Final conclusion
    print("Final Conclusion:")

    if accuracy >= 0.80:
        print("The Decision Tree model performs well.")
    else:
        print("The Decision Tree model needs improvement.")


if __name__ == "__main__":
    main()