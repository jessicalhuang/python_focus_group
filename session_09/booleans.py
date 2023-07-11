#!/usr/bin/env python3

bool1 = type(True)
print(bool1)

# Demonstrate Boolean as integer
bool2 = int(True)
print(bool2)
bool3 = int(False)
print(bool3)

# Demonstrate Boolean as float
bool4 = float(True)
print(bool4)
bool5 = float(False)
print(bool5)

# Type cast numeric to Boolean
bool6 = bool(1)
print(bool6)

bool7 = bool(0)
print(bool7)

# Variables
a = 5
b = 10
c = 5

# Determine if values are equal
IsEqual = a == b
print(IsEqual)

# Check if a value is greater than another
IsGreater = a > b
print(IsGreater)

# Check if a value is less than another
IsLess = a < b
print(IsLess)

# Check if a value is less than or equal to another
IsLessOrEqual = a <= c
print(IsLessOrEqual)

# Check if a value is greater than or equal to another
IsGreaterOrEqual = b >= c
print(IsGreaterOrEqual)

# See if values are not equal
IsNotEqual1 = a != b
print(IsNotEqual1)

IsNotEqual2 = a != c
print(IsNotEqual2)

# Check if strings match
str1 = "Hello, World!"
str2 = "Hello, World!"
str3 = "Hello World!"

print(str1 != str2)
print(str1 == str2)
print(str1 != str3)
print(str1 == str3)

# Compare letters
print("A" > "B")
print("A" < "B")

# Basic logic operators
print(not(True))
print(not(False))

# Using logic operators in a basic conditional
album_year = 1983
if album_year > 1979 and album_year < 1990:
    print("This album was made in the 80's")