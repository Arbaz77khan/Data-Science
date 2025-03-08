import numpy as np

def sigmoid(array):
    return 1/(1 + np.exp(-(array)))

a = np.arange(12).reshape(3,4)

s = sigmoid(a)

print(a)

print(s)