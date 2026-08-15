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
    student_data = pd.DataFrame(
        {
            "StudyHours":[1],
            "Attendance":[30],
            "PreviousScore":[50],
            "AssignmentsCompleted":[0],
            "SleepHours":[7]       
        }
    )
    prediction = model.predict(student_data)
    print("Prediction for the student is: ", prediction[0]) 
    

if __name__ == "__main__":
    main()