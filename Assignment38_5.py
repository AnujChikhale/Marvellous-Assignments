import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")

    print(df.groupby('FinalResult')['StudyHours'].mean())
    print(df.groupby('FinalResult')['Attendance'].mean())

if __name__ == "__main__":
    main()