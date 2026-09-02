import pandas as pd

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82],
        'Gender': ['M', 'M', 'F']
    }

    df = pd.DataFrame(data)

    print(df.groupby('Gender')[['Math','Science','English']].mean())

if __name__ == "__main__":
    main()