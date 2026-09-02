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

    amit = df[df['Name'] == 'Amit']
    plt.plot(
        ['Math','Science','English'],
        [amit['Math'].values[0],amit['Science'].values[0],amit['English'].values[0]],
        marker = 'o'
    )
    plt.title("Amit's subject wise marks")
    plt.show()

if __name__ == "__main__":
    main()