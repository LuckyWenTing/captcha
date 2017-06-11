from __future__ import division
from collections import Counter
from functools import partial
from linear_algebra import dot
import math, random
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

def step_function(x):
    return 1 if x >= 0 else 0


def perceptron_output(weights, bias, x):
    """returns 1 if the perceptron 'fires', 0 if not"""
    return step_function(dot(weights, x) + bias)


def sigmoid(t):
    return 1 / (1 + math.exp(-t))


def neuron_output(weights, inputs):
    a = sigmoid(dot(weights, inputs))
    #    print "\nneuron_output..."
    #    print "weights :", weights
    #    print "inputs :", inputs
    #    print "dot :", dot(weights, inputs)
    #    print "sigmoid :", a
    # input()
    return a


def feed_forward(neural_network, input_vector):
    """takes in a neural network (represented as a list of lists of lists of weights)
    and returns the output from forward-propagating the input"""

    outputs = []

    for layer in neural_network:
        input_with_bias = input_vector + [1]  # add a bias input
        #        print "layer: ", layer
        #        print "input with bias: \n", input_with_bias
        output = [neuron_output(neuron, input_with_bias)  # compute the output
                  for neuron in layer]  # for this layer
        outputs.append(output)  # and remember it

        # the input to the next layer is the output of this one
        input_vector = output

    return outputs


def backpropagate(network, input_vector, target):
    hidden_outputs, outputs = feed_forward(network, input_vector)
    #    print "\nhidden_outputs :", hidden_outputs
    #    print "outputs:", outputs
    #    for i, output in enumerate(outputs):
    #        print target[i]
    #    print "target:", target[i]


    # the output * (1 - output) is from the derivative of sigmoid
    output_deltas = [output * (1 - output) * (output - target[i])
                     for i, output in enumerate(outputs)]

    #    print "output_deltas :\n", output_deltas

    #    print "network[-1] before :\n", network[-1]
    # adjust weights for output layer (network[-1])
    for i, output_neuron in enumerate(network[-1]):
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            #            print "before: \n", output_neuron[j]
            #            print hidden_output
            #            print hidden_output * output_deltas[i]
            output_neuron[j] -= output_deltas[i] * hidden_output
            #            print "after : \n", output_neuron[j]

            #    print "network[-1] after  :\n", network[-1]

    # back-propagate errors to hidden layer
    hidden_deltas = [hidden_output * (1 - hidden_output) *
                     dot(output_deltas, [n[i] for n in network[-1]])
                     for i, hidden_output in enumerate(hidden_outputs)]

    # adjust weights for hidden layer (network[0])
    for i, hidden_neuron in enumerate(network[0]):
        for j, input1 in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input1


# input()


def patch(x, y, hatch, color):
    """return a matplotlib 'patch' object with the specified
    location, crosshatch pattern, and color"""
    return matplotlib.patches.Rectangle((x - 0.5, y - 0.5), 1, 1,
                                        hatch=hatch, fill=False, color=color)


def show_weights(neuron_idx):
    weights = network[0][neuron_idx]
    abs_weights = map(abs, weights)

    grid = [abs_weights[row:(row + 5)]  # turn the weights into a 5x5 grid
            for row in range(0, 25, 5)]  # [weights[0:5], ..., weights[20:25]]

    ax = plt.gca()  # to use hatching, we'll need the axis

    ax.imshow(grid,  # here same as plt.imshow
              cmap=matplotlib.cm.binary,  # use white-black color scale
              interpolation='none')  # plot blocks as blocks

    # cross-hatch the negative weights
    for i in range(5):  # row
        for j in range(5):  # column
            if weights[5 * i + j] < 0:  # row i, column j = weights[5*i + j]
                # add black and white hatches, so visible whether dark or light
                ax.add_patch(patch(j, i, '/', "white"))
                ax.add_patch(patch(j, i, '\\', "black"))
    plt.show()

def getPixel(file_name):
    im = Image.open(file_name)
    str2 = ""
    count = 0
    try:
        for i in range(im.size[0]):
            for j in range(im.size[1]):
                count+=1
                if (im.getpixel((i, j)) > 120):
                    str2 = "{0}{1}".format(str2, ".")
                else:
                    str2 = "{0}{1}".format(str2, "1")
                    # print "pixel [", i, j, "] : ", im.getpixel((i, j)), "\n"
    except Exception as e:
        print "Exception", e
    print "count:", count
    print "str:" + str2

    return str2

if __name__ == "__main__":
    raw_digits = []
    zero = getPixel("0_square.png")
    raw_digits.append(zero)
    zero = getPixel("1_square.png")
    raw_digits.append(zero)
    # raw_digits2 = [
    #         """11111
    #            1...1
    #            1...1
    #            1...1
    #            11111"""]
    print "raw_digits", raw_digits
    # print "raw_digits2", raw_digits2
            #
            # """..1..
            #    ..1..
            #    ..1..
            #    ..1..
            #    ..1..""",
            #
            # """11111
            #    ....1
            #    11111
            #    1....
            #    11111""",
            #
            # """11111
            #    ....1
            #    11111
            #    ....1
            #    11111""",
            #
            # """1...1
            #    1...1
            #    11111
            #    ....1
            #    ....1""",
            #
            # """11111
            #    1....
            #    11111
            #    ....1
            #    11111""",
            #
            # """11111
            #    1....
            #    11111
            #    1...1
            #    11111""",
            #
            # """11111
            #    ....1
            #    ....1
            #    ....1
            #    ....1""",
            #
            # """11111
            #    1...1
            #    11111
            #    1...1
            #    11111""",
            #
            # """11111
            #    1...1
            #    11111
            #    ....1
            #    11111""",
            #
            # """11111
            #    1...1
            #    ...11
            #    ....1
            #    11111""",
            #
            # """11111
            #    1...1
            #    .1111
            #    1...1
            #    11111""",
            #
            # """11111
            #    1...1
            #    ...11
            #    1...1
            #    11111"""]


    def make_digit(raw_digit):
        return [1 if c == '1' else 0
                for row in raw_digit.split("\n")
                for c in row.strip()]


    inputs = map(make_digit, raw_digits)  # 5*10

    targets = [[1 if i == j else 0 for i in range(13)]
               for j in range(13)]  # 10*10

    random.seed(0)  # to get repeatable results
    input_size = 40000  # each input is a vector of length 25
    num_hidden = 200  # we'll have 5 neurons in the hidden layer
    output_size = 2  # we need 10 outputs for each input

    # each hidden neuron has one weight per input, plus a bias weight
    hidden_layer = [[random.random() for __ in range(input_size + 1)]  # 26*5
                    for __ in range(num_hidden)]

    # each output neuron has one weight per hidden neuron, plus a bias weight
    output_layer = [[random.random() for __ in range(num_hidden + 1)]  # 6*10
                    for __ in range(output_size)]

    # the network starts out with random weights
    network = [hidden_layer, output_layer]

    #    print len(hidden_layer)
    #    print len(output_layer)
    #    print len(network)
    #    for i in range(len(network)):
    #        for j in range(len(network[i])):
    #            print network[i][j]
    # print network[i]

    #    print inputs
    #    print targets
    print "zip:", zip(inputs, targets)

    # 10,000 iterations seems enough to converge
    for __ in range(1000):
        #        input()
        #        print "iter = ", __
        for input_vector, target_vector in zip(inputs, targets):
            backpropagate(network, input_vector, target_vector)

    # print target_vector
    # for i in range(len(network)):
    #     for j in range(len(network[i])):
            # print network[i][j]


    def predict(input):
        return feed_forward(network, input)[-1]


    for i, input in enumerate(inputs):
        outputs = predict(input)
        print i, [round(p, 2) for p in outputs]
#
#     print """@@@@@
# @...@
# ..@@@
# @...@
# @@@@@"""
#     print [round(x, 2) for x in
#            predict([0, 1, 1, 1, 0,  # .@@@.
#                     0, 1, 0, 1, 0,  # ...@@
#                     0, 1, 0, 1, 0,  # ..@@.
#                     0, 1, 0, 1, 0,  # ...@@
#                     0, 1, 1, 1, 0])  # .@@@.
#            ]
#     print
#
#     print """@@@@@
# @...@
# ...@@
# ....@
# @@@@@"""
#
#     print [round(x, 2) for x in
#            predict([1, 1, 1, 1, 1,  # .@@@.
#                     1, 0, 0, 0, 1,  # ...@@
#                     0, 0, 0, 1, 1,  # ..@@.
#                     0, 0, 0, 0, 1,  # ...@@
#                     1, 1, 1, 1, 1])  # .@@@.
#            ]
#     print

# print """@@@@@
# @...@
# ..@@@
# ....@
# @@@@@"""
#
#    print [round(x, 2) for x in
#       predict(  [1,1,1,1,1,  # .@@@.
#                  1,0,0,0,1,  # ...@@
#                  0,0,0,1,1,  # ..@@.
#                  0,0,0,0,1,  # ...@@
#                  1,1,1,1,1]) # .@@@.
#       ]
#    print

#    print """.@@@.
# @..@@
# .@@@.
# @..@@
# .@@@."""
#    print [round(x, 2) for x in
#          predict(  [0,1,1,1,0,  # .@@@.
#                     1,0,0,1,1,  # @..@@
#                     0,1,1,1,0,  # .@@@.
#                     1,0,0,1,1,  # @..@@
#                     0,1,1,1,0]) # .@@@.
#          ]
#    print

