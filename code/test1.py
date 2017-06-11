from __future__ import division
from collections import Counter
from functools import partial
from linear_algebra import dot
import math, random
import matplotlib
import matplotlib.pyplot as plt

def step_function(x):
    return 1 if x >= 0 else 0

def perceptron_output(weights, bias, x):
    """returns 1 if the perceptron 'fires', 0 if not"""
    return step_function(dot(weights, x) + bias)

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))

def feed_forward(neural_network, input_vector):
    """takes in a neural network (represented as a list of lists of lists of weights)
        and returns the output from forward-propagating the input"""
    
    outputs = []
    
    for layer in neural_network:
        
        input_with_bias = input_vector + [1]             # add a bias input
        print "layer = ", layer
        print "input with bias = ", input_with_bias
        output = [neuron_output(neuron, input_with_bias) # compute the output
                  for neuron in layer]                   # for this layer
        outputs.append(output)                           # and remember it
                  
                  # the input to the next layer is the output of this one
        input_vector = output
    
    return outputs


if __name__ == "__main__":
    xor_network = [[[20, 20, -30], [20, 20, -10]], [[-60, 60, -30]]]
    for x in [0,1]:
        for y in [0,1]:
            print x, y, feed_forward(xor_network, [x,y])