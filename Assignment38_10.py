import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.scatter(df["FinalResult"], df["SleepHours"])

    plt.xlabel("Final Result")
    plt.ylabel("Sleep Hours")
    plt.title("Sleep Hours vs Final Result")

    plt.show()


if __name__ == "__main__":
    main()