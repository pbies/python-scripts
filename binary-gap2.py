#!/usr/bin/env python3

def binary_gap(n):
    binary = bin(n)[2:]  # Convert the integer to binary representation and remove the '0b' prefix
    max_gap = 0
    current_gap = 0
    for digit in binary:
        if digit == '0':
            current_gap += 1
        else:
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
    return max_gap

# Example usage:
number = 1041
gap = binary_gap(number)
print(gap)
