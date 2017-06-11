import math
from linear_algebra import dot


def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neuron_output(weights, inputs):
    a = sigmoid(dot(weights, inputs))
    print "weights :", weights
    print "inputs :", inputs
    print "dot :", dot(weights, inputs)
    print "sigmoid :", a
    return a


print sigmoid(0)
print sigmoid(1)
print neuron_output([0.9],[1])