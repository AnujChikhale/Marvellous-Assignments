from sklearn.metrics import confusion_matrix, classification_report

Actual = [1,1,1,1,0,0,0,0]
Predicted = [1,1,0,1,0,1,0,0]
print(classification_report(Actual, Predicted))