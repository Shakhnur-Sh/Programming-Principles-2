from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

def square(x):
    return x * x

def is_even(x):
    return x % 2 == 0

def add(a, b):
    return a + b

# Using map, filter, and reduce
squares = list(map(square, numbers))
print("Squares:", squares)

even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

total = reduce(add, numbers)
print("Sum using reduce:", total)

# Demonstrating type checking and conversions
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print("Original type:", type(num_str))
print("Converted to int:", num_int, type(num_int))
print("Converted to float:", num_float, type(num_float))