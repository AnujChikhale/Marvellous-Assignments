import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier

df = pd.read_csv('Customer_Loan_Approval.csv')

print(df.isnull().sum())

X = df.drop('LoanApproved',axis = 1)
Y = df['LoanApproved']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.7,random_state=42)

model1 = LogisticRegression(max_iter=1000)
model2 = DecisionTreeClassifier(random_state=42)
model3 = KNeighborsClassifier(n_neighbors=5)

model1 = model1.fit(X_train, Y_train)
Y1_pred = model1.predict(X_test)
print("Accuracy score of model1 is : ",accuracy_score(Y_test,Y1_pred))

model2 = model2.fit(X_train, Y_train)
Y2_pred = model2.predict(X_test)
print("Accuracy score of model2 is : ",accuracy_score(Y_test,Y2_pred))

model3 = model3.fit(X_train, Y_train)
Y3_pred = model3.predict(X_test)
print("Accuracy score of model3 is : ",accuracy_score(Y_test,Y3_pred))


model4 = VotingClassifier(
    estimators=[
        ('logistic',model1),
        ('decision_tree',model2),
        ('knn',model3)
    ],
    voting='hard'
)

model4 = model4.fit(X_train,Y_train)
Y_pred4 = model4.predict(X_test)

print("Accuracy for Hard voting is: ", accuracy_score(Y_test,Y_pred4))

model5 = VotingClassifier(
    estimators=[
        ('logistic',model1),
        ('decision_tree',model2),
        ('knn',model3)
    ],
    voting='soft'
)

model5 = model5.fit(X_train,Y_train)
Y_pred5 = model5.predict(X_test)

print("Accuracy for Soft voting is: ", accuracy_score(Y_test,Y_pred5))
