import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.boxplot(
        [
            df["FinalResult"],
            df["AssignmentsCompleted"]
        ]
        

    )
    plt.xlabel("Final Result")
    plt.ylabel("Assignments completed")
    plt.title("Assignments completed vs Final result")
    plt.show()

if __name__ == "__main__":
    main()