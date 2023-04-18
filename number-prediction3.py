#!/usr/bin/env python3
import numpy as np
import tensorflow as tf

def predict_number(sequence):
    if len(sequence) < 2:
        return None
    
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(32, activation='relu', input_shape=(1,)))
    model.add(tf.keras.layers.Dense(16, activation='relu'))
    model.add(tf.keras.layers.Dense(1))
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    X = np.array(range(len(sequence))).reshape(-1, 1)
    y = np.array(sequence)
    
    model.fit(X, y, epochs=100)
    
    next_index = np.array([len(sequence)]).reshape(1, -1)
    next_number = model.predict(next_index)[0][0]
    
    return next_number

# Example usage
sequence = [1, 2, 4, 7, 11]
next_number = predict_number(sequence)
print("The next number in the sequence is:", next_number)
