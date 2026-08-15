import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("Average study hour is: ",df["StudyHours"].mean())
print("Average of Attendence is: ",df["Attendance"].mean())
print("Maximum of previous score is: ",df["PreviousScore"].max())
print("Minimum sleephour is: ",df["SleepHours"].min())
