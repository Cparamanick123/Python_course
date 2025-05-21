
'''ASSIGNMENT 3:
Module 4: Functions & Modules in Python 
Task 1: Calculate Factorial Using a Function 
'''

def factorial_iterative(n):
    """Calculate factorial using an iterative approach (loop)"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Get user input
num = int(input("Enter a number: "))

# Calculate factorial using both methods
iterative_result = factorial_iterative(num)
recursive_result = factorial_recursive(num)

# Print the results
print(f"Factorial of {num} (uing iterative) is: {iterative_result}")
print(f"Factorial of {num} (using recursive) is: {recursive_result}")


import math

# Get user input
number = float(input("Enter a number: "))

# Calculate using math module functions
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)  # Note: input is in radians

# Display the results
print(f"\nCalculations for {number}:")
print(f"Square root: {square_root:.4f}")
print(f"Natural logarithm: {natural_log:.4f}")
print(f"Sine (in radians): {sine_value:.4f}")