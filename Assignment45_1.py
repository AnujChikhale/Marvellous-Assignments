import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    }

    df = pd.DataFrame(data)
    print(df)

    scalar = MinMaxScaler()

    df['Math'] = scalar.fit_transform(df[['Math']])
    print(df)

if __name__ == "__main__":
    main()