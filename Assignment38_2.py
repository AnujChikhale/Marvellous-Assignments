import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("Total number of students are: ", len(df))
print("Count of student passed is: ", (df["FinalResult"] == 1).sum())
print("Count of student failed is: ", (df["FinalResult"] == 0).sum())
