import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82],
        'Gender': ['M', 'M', 'F']
    }

    df = pd.DataFrame(data)

    sagar = df[df['Name']=='Sagar'][['Math','Science','English']].values.flatten()
    labels = ['Math','Science','English']
    plt.pie(sagar, labels=labels, autopct='%1.1f%%')
    plt.title("Sagars Subject wise distribution")
    plt.show()

if __name__ == "__main__":
    main()