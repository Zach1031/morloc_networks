from typing import final
import numpy

def cost_derivative(output, desired_output):
    return output- desired_output

def quadratic_cost(output, desired_output):
    return 0.5*numpy.linalg.norm(output-desired_output)**2

def quadratic_delta(output, desired_output, final_output,cost_derivative):
    return (output-desired_output) * cost_derivative(final_output)

def cross_entropy_cost(output, desired_output):
    return numpy.sum(numpy.nan_to_num((-desired_output * numpy.log(output)) - ((1 - desired_output) * numpy.log(1 - output))))

# included for uniformity with quadratic_delta incase they are used concurently
def cross_entropy_delta(output, desired_output, final_output=None, cost_derivative=None):
    return output-desired_output