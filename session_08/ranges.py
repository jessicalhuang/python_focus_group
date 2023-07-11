#!/usr/bin/env python3

# Turn our range into a list
numbers = list(range(1,6))
print(numbers)

# Turn our range into a list containing numbers 1-20
range1_20 = list(range(1,21))
print(range1_20)

# Skipping numbers in a given range:
# (first number, last number + 1, every nth value you want)
# Even numbers from 1-10
even_numbers = list(range(2, 11, 2))
print(even_numbers)