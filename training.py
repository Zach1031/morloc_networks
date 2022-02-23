import numpy

def feedforward(a, biases, weights, activation):     
    for b, w in zip(biases, weights):
        a = activation(numpy.dot(w, a)+b)
    return a

def backpropigation(biases, weights, x, y, activation_function, activation_derivative, cost_derivative, layers):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [numpy.zeros(b.shape) for b in biases]
        nabla_w = [numpy.zeros(w.shape) for w in weights]
        # feedforward
        activation = x
        activations = [x] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(biases, weights):
            z = numpy.dot(w, activation)+b
            zs.append(z)
            activation = activation_function(z)
            activations.append(activation)
        # backward pass
        delta = cost_derivative(activations[-1], y) * \
            activation_derivative(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = numpy.dot(delta, activations[-2].transpose())
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in range(2, layers):
            z = zs[-l]
            sp = activation_derivative(z)
            delta = numpy.dot(weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = numpy.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)