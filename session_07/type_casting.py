#!/usr/bin/env python3

# Assign numbers as an integer, floaat, and string
a = 1
b = 1.5
c = '1'

# Demonstrate type incompatabilities
print(a + b)

print(type(a))
print(type(b))

# Store float in d
d = 1.9
print(d, type(d))

# Convert float from d to integer and store in e
e = int(d)
print(e, type(e))

# Functions for type casting

# Turn the string "3" into an integer
my_int = int("3")
print(my_int, type(my_int))

# Turn the number 53 into a string
my_str = str(53)
print(my_str, type(my_str))

# Turn the integer 7 into a float
my_float = float(7)
print(my_float, type(my_float))