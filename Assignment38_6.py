import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.hist(df["StudyHours"])
    plt.title("Student's Study-Hour analysis")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()