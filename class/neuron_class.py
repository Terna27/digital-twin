
class Neuron:
    
    def __init__(self, weight, bias):
        
        self.weight = weight
        self.bias = bias
        
    def calculate(self, inputs):
        
        total = 0
        for i in range(len(inputs)):
            
            total = inputs[i] * self.weight[i]
            sum_total = total + self.bias
            
        return sum_total
    
def run():
    
    neuron1 = Neuron([0.5, 0.8], -0.2)

    result = neuron1.calculate([2, 3])

    print(result)