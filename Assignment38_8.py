import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.boxplot(
        df,
        meanline=True,
    )
    plt.title("Students attendence")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()