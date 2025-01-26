# implementation of the perceptron algorithm

import numpy as np
class perceptron:
    def __init__(self, leraning_rate=0.01, n_iter=100):
        self.lr = leraning_rate
        self.iter = n_iter
        self.weights = None
        self.bias = None
        
        def activation_fuction(self,z):
            return 1 if z >= 0 else 0
        
        def fit(self,X,y):
            n_samples, n_features = X.shape
            self.weights = np.zeros(n_features)
            self.bias = 0
            
            for _ in range(self.iter):
                for idx, x_i in enumerate(X):
                    z = np.dot(x_i, self.weights) + self.bias
                    ypred = self.activation_function(z)
                    update = self.lr * (y[idx]-ypred)
                    self.weights += update * x_i
                    self.bias += update
                    
        def predict(self,X):
            z = np.dot(X, self.weights) + self.bias
            return np.array([self.activation_function(z_i) for z_i in z])