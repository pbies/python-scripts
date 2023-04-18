#!/usr/bin/env python3

def binary_gap(n):
    # Convert integer to binary string
    binary = bin(n)[2:]

    # Initialize variables
    max_gap = 0
    current_gap = 0
    counting = False

    # Iterate through binary string
    for digit in binary:
        if digit == '1':
            # Found a 1, start counting gap
            counting = True
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
        elif counting:
            # Counting gap
            current_gap += 1

    return max_gap
