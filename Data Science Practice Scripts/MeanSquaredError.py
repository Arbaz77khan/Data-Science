import numpy as np

def MSE(x, y):
    return np.mean((x - y)**2)

actual_Age_DataSet = np.random.randint(18, 70, 10)
Predicted_Age_DataSet = np.random.randint(18, 70, 10)

print(actual_Age_DataSet, "\n", Predicted_Age_DataSet)

print(MSE(actual_Age_DataSet, Predicted_Age_DataSet))

     