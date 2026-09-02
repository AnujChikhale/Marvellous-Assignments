import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82],
        'Gender': ['M', 'M', 'F']
    }

    df = pd.DataFrame(data)
    df['Gender'] = ['M', 'M', 'F']

    df['Total'] = df['Math']+df['Science']+df['English']

    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x>=250 else 'Fail')

    df.rename(columns={'Math': 'Mathematics'}, inplace=True)
    print(df)

if __name__ == "__main__":
    main()