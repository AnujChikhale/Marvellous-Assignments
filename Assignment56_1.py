import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier,AdaBoostClassifier,VotingClassifier


df = pd.read_csv('Fraudulent_Transaction_Detection.csv')
print(df.head())

X = df.drop('Fraud', axis=1)
Y = df['Fraud']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

DT_model = DecisionTreeClassifier(random_state=42)
DT_model = DT_model.fit(X_train,Y_train)
DT_Y_pred = DT_model.predict(X_test)
print("Accuracy for decision tree is : ",accuracy_score(Y_test,DT_Y_pred))
print("Precision for decision tree is : ",precision_score(Y_test,DT_Y_pred))
print("Recall for decision tree is : ",recall_score(Y_test,DT_Y_pred))
print("F1 score for decision tree is : ",f1_score(Y_test,DT_Y_pred))
print("Confusion matrix for decision tree is : ",confusion_matrix(Y_test,DT_Y_pred))


B_model = BaggingClassifier(n_estimators=1000)
B_model = B_model.fit(X_train,Y_train)
B_Y_pred = B_model.predict(X_test)
print("Accuracy for Bagging is : ",accuracy_score(Y_test,B_Y_pred))
print("Precision for Bagging is : ",precision_score(Y_test,B_Y_pred))
print("Recall for Bagging is : ",recall_score(Y_test,B_Y_pred))
print("F1 score for Bagging is : ",f1_score(Y_test,B_Y_pred))
print("Confusion matrix for Bagging is : ",confusion_matrix(Y_test,B_Y_pred))

RF_model = RandomForestClassifier(n_estimators=1000)
RF_model = RF_model.fit(X_train,Y_train)
RF_Y_pred = RF_model.predict(X_test)
print("Accuracy for Random Forest is : ",accuracy_score(Y_test,RF_Y_pred))
print("Precision for Random Forest is : ",precision_score(Y_test,RF_Y_pred))
print("Recall for Random Forest is : ",recall_score(Y_test,RF_Y_pred))
print("F1 score for Random Forest is : ",f1_score(Y_test,RF_Y_pred))
print("Confusion matrix for Random Forest is : ",confusion_matrix(Y_test,RF_Y_pred))

AB_model = AdaBoostClassifier(n_estimators=1000)
AB_model = AB_model.fit(X_train,Y_train)
AB_Y_pred = AB_model.predict(X_test)
print("Accuracy for AdaBoost is : ",accuracy_score(Y_test,AB_Y_pred))
print("Precision for AdaBoost is : ",precision_score(Y_test,AB_Y_pred))
print("Recall for AdaBoost is : ",recall_score(Y_test,AB_Y_pred))
print("F1 score for AdaBoost is : ",f1_score(Y_test,AB_Y_pred))
print("Confusion matrix for AdaBoost is : ",confusion_matrix(Y_test,AB_Y_pred))

V_model = VotingClassifier(
    estimators=[
        ('random_forest', RF_model),
        ('decision_tree', DT_model),
        ('bagging', B_model)
    ],
    voting='hard'
)
V_model = V_model.fit(X_train,Y_train)
V_Y_pred = V_model.predict(X_test)
print("Accuracy for VotingClassifier is : ",accuracy_score(Y_test,V_Y_pred))
print("Precision for VotingClassifier is : ",precision_score(Y_test,V_Y_pred))
print("Recall for VotingClassifier is : ",recall_score(Y_test,V_Y_pred))
print("F1 score for VotingClassifier is : ",f1_score(Y_test,V_Y_pred))
print("Confusion matrix for VotingClassifier is : ",confusion_matrix(Y_test,V_Y_pred))
