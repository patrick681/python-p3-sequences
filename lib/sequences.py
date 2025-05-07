#!/usr/bin/env python3

def print_fibonacci(length):
    # Handle edge case for length 0
    if length == 0:
        print("[]")
        return
    
    # Special case: if length is 1, print [0]
    if length == 1:
        print("[0]")
        return
    
    # Special case: if length is 2, print [0, 1]
    if length == 2:
        print("[0, 1]")
        return
    
    # Initialize the Fibonacci sequence for lengths greater than 2
    fib_sequence = [0, 1]

    # Generate Fibonacci sequence up to the desired length
    while len(fib_sequence) < length:
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Sum of the last two elements
        fib_sequence.append(next_fib)
    
    # Print the Fibonacci sequence as a list
    print(fib_sequence[:length])
