import pandas as pd


df = pd.read_csv("student_performance_ml.csv")

print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.columns)
print(df.columns.dtype)