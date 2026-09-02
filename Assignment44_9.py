import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan,90,78],
        'Science': [92,np.nan,80]
    }

    df = pd.DataFrame(data)
    df = df.fillna(value=df.mean(numeric_only=True))
    print(df)


if __name__ == "__main__":
    main()