import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")

    print(df.head())
    print(df["FinalResult"].value_counts())

    pass_student = df[df["FinalResult"] == "Pass"]
    fail_student = df[df["FinalResult"] == "Fail"]

    plt.scatter(
        pass_student["StudyHours"],
        pass_student["PreviousScore"],
        color="green",
        label="Pass"
    )

    plt.scatter(
        fail_student["StudyHours"],
        fail_student["PreviousScore"],
        color="red",
        label="Fail"
    )

    plt.xlabel("Study Hour")
    plt.ylabel("Previous Score")
    plt.title("StudyHour VS PreviousScore")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()