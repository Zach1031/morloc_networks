import numpy
sizes = [1,2,3]

test = [numpy.random.randn(y, 1) for y in sizes[1:]]

weights = []
for i in range(1, len(sizes)):
    temp_list = []
    for j in range (0, i+1):
        temp_list.append([numpy.random.normal(0, (2.0 / (sizes[i-1] + sizes[i])))])
    weights.append(temp_list)
print(weights[0])
print(test[0])
