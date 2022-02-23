import numpy

def sigmoid(z = None):
    if(z == None):
        return 0
    return 1.0/(1.0+numpy.exp(-z))

def feedforward(a, biases, weights):
    for b, w in zip(biases, weights):
        a = sigmoid(numpy.dot(w, a)+b)
    return a

def int_list(list):
    return list

print(sigmoid())
print(sigmoid(2))
