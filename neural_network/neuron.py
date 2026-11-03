
import numpy as np

# # # maths = 80
# # # English = 70

# # # mweight = 0.6
# # # Eweight = 0.3


# # # weightes_sum = ( 
# # #     maths * mweight + English * Eweight
# # # )
# # # print(f"{weightes_sum}%")

# # def neuron(math, eng):
    
# #     math_weight = 0.6
# #     eng_weight = 0.4
    
# #     weighted_sum = (
# #         math * math_weight + eng * eng_weight
# #     )
    
# #     return weighted_sum
    
# # result1 = neuron(80, 70)
# # result2 = neuron(60, 50)
# # print(result1)
# # print(result2)

# # def calculate_neuron(x1, x2, bias):
  
# #   w1 = 0.7
# #   w2 = 0.3
  
# #   weighted_sum = (
# #       x1 * w1 + x2 * w2
# #   )
  
# #   with_bias = weighted_sum + bias
# #   return with_bias

# # def activation(z):
# #     if z >= 0 :
# #         return 1
# #     else:
# #         return 0

# # def run():
    
# #     result = calculate_neuron(6, 8, -1.5)
    
# #     print(result)
# #     output = activation(result)
    
# #     print(output)

# # def activation(z):
# #     if z >= 0:
# #         return 1
# #     else:
# #         return 0


# # def perceptron(x1, x2):
# #     w1 = 0.6
# #     w2 = 0.6
# #     bias = -1.0

# #     # Calculate weighted sum with bias
# #     weighted_sum = (
# #         x1*w1 + x2*w2    
# #         ) + bias
    
    
# #     output = activation(weighted_sum)
    
# #     return output
  


# # def run():
# #     inputs = [
# #         (0, 0),
# #         (0, 1),
# #         (1, 0),
# #         (1, 1)
# #     ]

# #     for x1, x2 in inputs:
# #         # Call the perceptron
# #         result = perceptron(x1, x2)
# #         # Print the inputs and prediction
# #         print(result)
        



# inputs = [[1.2, 2.4, 0.3, 4], [0.2, 1.4, 0.3, -1], [1.2, -1.1, 0.3, 3]]


# weights = [[0.6, 0.9, -1.2, 0.5], [0.1, 0.5, 1, 0.3], [0.12, 0.3, 0.2, 0.5]]

# weights2 = [[0.6, 0.9, -1.2, 0.5], [0.1, 0.5, 1, 0.3], [0.12, 0.3, 0.2, 0.5]]
            
# biases = [-1, 2.0, 0.5]
# biases2 = [1, -1.0, 0.2]

# layer1_output = np.dot(inputs, np.array(weights).T) + biases
# # layer2_output = np.dot(inputs, np.array(weights2).T) + biases2

# print(f"{layer1_output}")



inputs = np.array([3, 5])
weights = np.array([0.4, 0.6])
bias = -1.5

weighted_sum = np.dot(inputs, weights) + bias

print(weighted_sum)

