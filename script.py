"""
This script demonstrates the use of functions imported from the simple_functions module.
It includes examples of doubling and squaring a number.

Functions:
    double_number: Doubles the input number.
    square_number: Squares the input number.

Usage:
    Run the script to see the output of the functions with the example value.
"""
from simple_functions import double_number, square_number

a = 5

print(f'value before double_number(): {a}')
result = double_number(a)
print(f'value after double_number(): {result}')

print(f'value before square_number(): {a}')
result = square_number(a)
print(f'value after square_number(): {result}')
