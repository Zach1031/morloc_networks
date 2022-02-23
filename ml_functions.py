import numpy

def feedforward(a, biases, weights):
    for b, w in zip(biases, weights):
        a = sigmoid(numpy.dot(w, a)+b)
    return a

def cost_derivative(output_activations, y):
    return (output_activations-y)
