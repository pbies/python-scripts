#!/usr/bin/env python3
def predict_number(sequence):
    if len(sequence) < 2:
        return None
    
    # Calculate the average difference between consecutive numbers
    differences = [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]
    average_difference = sum(differences) / len(differences)
    
    # Predict the next number in the sequence
    next_number = sequence[-1] + average_difference
    
    return next_number

# Example usage
sequence = [1, 2, 4, 7, 11]
next_number = predict_number(sequence)
print("The next number in the sequence is:", next_number)
