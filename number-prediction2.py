#!/usr/bin/env python3
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_number(sequence):
    if len(sequence) < 2:
        return None
    
    X = np.array(range(len(sequence))).reshape(-1, 1)
    y = np.array(sequence)
    
    model = LinearRegression()
    model.fit(X, y)
    
    next_index = len(sequence)
    next_number = model.predict([[next_index]])[0]
    
    return next_number

# Example usage
sequence = [1, 2, 4, 7, 11]
next_number = predict_number(sequence)
print("The next number in the sequence is:", next_number)
