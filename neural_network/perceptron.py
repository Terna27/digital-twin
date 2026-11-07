import numpy as np

inputs = np.array([1, 1])
weights = np.array([0.2, 0.3])
bias = -0.8

learning_rate = 0.1
target = 1

weighted_sum = np.dot(inputs, weights) + bias
prediction = 1 if weighted_sum >= 0 else 0

error = target - prediction

weights = weights + learning_rate * error * inputs
bias = bias + learning_rate * error

print("Prediction:", prediction)
print("Error:", error)
print("Updated weights:", weights)
print("Updated bias:", round(bias, 2))