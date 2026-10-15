import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score,f1_score

df = pd.read_csv('Loan_Default.csv')

print(df.isnull().sum())

df['PreviousDefault'] = df['PreviousDefault'].map({
    'No':0,
    'Yes':1
})

df = pd.get_dummies(df, columns=['HomeOwnership'], dtype=int)

X = df.drop('Default', axis =1)
Y = df['Default']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

model = MLPClassifier(
    hidden_layer_sizes=(100,50,25),
    activation='identity',
    solver='adam',
    max_iter=1000,
    random_state=42,
    learning_rate_init=0.1
)

model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

print("Accuracy is: ", accuracy_score(Y_pred,Y_test))
print("Confusion matrix: ", confusion_matrix(Y_pred,Y_test))
print("Classification report: ", classification_report(Y_pred,Y_test))
print("Precision score is: ", precision_score(Y_pred,Y_test))
print("Recall is: ", recall_score(Y_pred,Y_test))
print("F1 score is: ", f1_score(Y_pred,Y_test))

# plt.plot(model.loss_curve_)
# plt.xlabel('Number of Iterations')
# plt.ylabel('Loss')
# plt.title('Loss Curve')
# plt.grid(True)
# plt.show()