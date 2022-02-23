import numpy

def gaussian_weights(sizes):
    return [numpy.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

def gaussian_biases(sizes):
    return [numpy.random.randn(y, 1) for y in sizes[1:]]


def glorot_gaussian_weights(sizes):
    weights = []
    for i in range(0, len(sizes)-1):
        for j in range(0, sizes[i+1]):
            temp_list = []
            for k in range(0, sizes[i]):
                temp_list.append(numpy.random.normal(0, (2.0 / (sizes[i-1] + sizes[i]))))
            weights.append(temp_list)
    return weights

def glorot_guassian_biases(sizes):
    biases = []
    for i in range(1, len(sizes)):
        temp_list = []
        for j in range (0, i+1):
            temp_list.append([numpy.random.normal(0, (2.0 / (sizes[i-1] + sizes[i])))])
        biases.append(temp_list)
    return biases

def glorot_uniform_weights(sizes):
    weights = []
    for i in range(0, len(sizes)-1):
        for j in range(0, sizes[i+1]):
            temp_list = []
            for k in range(0, sizes[i]):
                temp_list.append(numpy.random.uniform((-(numpy.sqrt(6)) / numpy.sqrt((sizes[i-1] + sizes[i])), (numpy.sqrt(6) / numpy.sqrt((sizes[i-1] + sizes[i]))))))
            weights.append(temp_list)
    return weights

def glorot_uniform_biases(sizes):
    biases = []
    for i in range(1, len(sizes)):
        temp_list = []
        for j in range (0, i+1):
            temp_list.append([numpy.random.uniform((-(numpy.sqrt(6)) /
            numpy.sqrt((sizes[i-1] + sizes[i])), (numpy.sqrt(6) / numpy.sqrt((sizes[i-1] + sizes[i])))))])
        biases.append(temp_list)
    return biases

if __name__ == "__main__":
    print("Gaussian weights: ", (gaussian_weights([3,2,3])))
    print("Gaussian biases: ", (gaussian_biases([3,2,3])))
    print("Glorot Gaussian weights: ", (glorot_gaussian_weights([3,2,3])))
    print("Glorot Gaussian biases: ", (glorot_guassian_biases([3,2,3])))
    print("Glorot Uniform weights: ", (glorot_uniform_weights([3,2,3])))
    print("Glorot Uniform biases: ", (glorot_uniform_biases([3,2,3])))
