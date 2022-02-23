#include<cmath>

double step(double x){
  return x >= 0 ? 1 : 0;
}

double sigmoid(double x){
  return 1.0/(1.0+exp(-x));
}

double sigmoid_prime(double x){
  return sigmoid(x)*(1-sigmoid(x));
}

double tanh(double x){
  return (exp(x)-exp(-x))/(exp(x)+exp(-x));
}

double tanh_prime(double x){
  return 2 / (exp(x) + exp(-x));
}

double relu(double x){
  return x > 0 ? x : 0;
}
