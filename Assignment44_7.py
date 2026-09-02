import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    }

    df = pd.DataFrame(data)

    df['Total'] = df['Math']+df['Science']+df['English']

    df = df.sort_values(by='Total', ascending=False)

    plt.bar(
        df['Name'],
        df['Total'],

    )
    plt.xlabel('Student name')
    plt.ylabel('Total marks')
    plt.title("Bar plot")
    plt.show()

if __name__ == "__main__":
    main()