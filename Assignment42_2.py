import math

def EuclidianDistance(p1,p2):
    Ans = math.sqrt((p1['X']-p2['X'])**2 + (p1['Y']-p2['Y'])**2)
    return Ans

def KNN(p,k=3):
    border = '-'*30

    Data = [
        {'point':'A', 'X':1, 'Y': 2, 'label':'Red'},
        {'point':'B', 'X':2, 'Y': 3, 'label':'Red'},
        {'point':'C', 'X':3, 'Y': 1, 'label':'Blue'},
        {'point':'D', 'X':6, 'Y': 5, 'label':'Blue'}
    ]

    for d in Data:
        d['Distance'] = EuclidianDistance(p,d)

    sorted_data = sorted(Data, key = lambda item : item['Distance'])

    k_nearest = sorted_data[:k]
    for d in k_nearest:
        print(d)

    votes={}
    for neighbor in k_nearest:
        label = neighbor['label']
        votes[label] = votes.get(label,0) + 1

    for d in votes:
        print("Name:",d,"Votes:",votes[d])

    iMax=0
    Name=""
    for d in votes:
        if(votes[d]>iMax):
            iMax=votes[d]
            Name = d
    print("Final prediction is: ",Name)
    print("For K = ",k)

def main():
    X = int(input("Enter X Cordinate: "))
    Y = int(input("Enter Y Cordinate: "))
    p = {'X':X, 'Y':Y}
    KNN(p,1)
    KNN(p,3)
    KNN(p,5)

#The prediction changes with k because it tells how many nearest points to be considered


if __name__ == "__main__":
    main()
