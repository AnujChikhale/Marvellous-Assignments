from sklearn.metrics import confusion_matrix

Actual = [1,1,1,1,0,0,0,0]
Predicted = [1,1,0,1,0,1,0,0]
print(confusion_matrix(Actual, Predicted))