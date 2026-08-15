import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")

    values_count = df["FinalResult"].value_counts()
    print(values_count)

    percent_count = (df["FinalResult"].value_counts()/len(df["FinalResult"])) * 100
    print(percent_count)

if __name__ == "__main__":
    main()