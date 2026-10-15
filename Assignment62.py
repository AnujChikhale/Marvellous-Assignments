import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv("Employee_Attrition.csv")
print(df.head())
print("Shape of dataset is : ",df.shape)
print("Columns of dataset: ",df.columns)

print(df.isnull().sum())

df['OverTime'] = df['OverTime'].map({'No': 0, 'Yes': 1})
df['Attrition'] = df['Attrition'].map({'No': 0, 'Yes': 1})

X = df.drop('Attrition', axis = 1)
Y = df['Attrition']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)
model.fit(X_train, Y_train)

print("Iteration required: ", model.n_iter_)

print("Training accuracy: ", model.score(X_train, Y_train))
print("Testing accuracy: ", model.score(X_test, Y_test))

Y_pred = model.predict(X_test)

print("Confusion Matrix: ", confusion_matrix(Y_test,Y_pred))

plt.plot(model.loss_curve_)
plt.xlabel("Iteration (Epochs)")
plt.ylabel("Loss")
plt.title("MLPClassifier Loss Curve")
plt.grid(True)
plt.show()