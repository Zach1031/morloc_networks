import numpy


def step(x):
    1 if x >= 0 else 0

def sigmoid(x):
    return 1.0/(1.0+numpy.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

def tanh(x):
    return (numpy.exp(x) - numpy.exp(-x)) / (numpy.exp(x) + numpy.exp(-x))

def tanh_prime(x):
    return 2 / (numpy.exp(x) + numpy.exp(-x))

def relu(x):
    return x if x >= 0 else 0

def relu_prime(x):
    return 1 if x >= 0 else 0

def param_relu(x, scalar = .01):
    return x if x >= 0 else scalar * x

def param_relu_prime(x, scalar = .01):
    return 1 if x >= 0 else scalar

def elu(x, scalar = 1):
    return x if x >= 0 else scalar * (numpy.exp(x-1))

def swish(x):
    return x * (1.0/(1.0+numpy.exp(-x)))
