#!/usr/bin/env python3

# Make an if-else statement
age = 16

if age >=18:
    print("You may enter!")
else:
    print("You are too young to enter.")

age = 14
print("Dad: Happy birthday! How old are you turning this year?")
print(f"Son: Thank you. I'm turning {age} this year")
if age >= 16:
    print("Dad: Good, now go get a job")
else:
    print(f"Dad: Wow, only {16-age} more years until you can get a job")

# Make a conditional statement with elif (else if)
x = 5
y = 10

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# Using 'and' in conditional statements
age = 20

if age >= 18 and age <21:
    print("You may enter!")
elif age < 18:
    print("You're too young!")
else:
    print("This club is not for you.")

# Using 'or' in conditional statements
marble = "green"

if marble == "blue" or marble == "green":
    print("Yay! This is one of my favorite colors.")
else:
    print("Oh no, I wanted a different color.")

if marble == "blue" and marble == "green":
    print("Yay! This is one of my favorite colors.")
else:
    print("Oh no, I wanted a different color.")

my_pets = ["Iguana", "Bird"]

if "Gecko" in my_pets:
    print("Ooh! Viki has a gecko!")

print("We have now passed the conditional")

# Original list
my_numbers = [74, 60, 4, 93, 2, 1, 54]

# New lists
single_digits = []
double_digits = []

for num in my_numbers:
    if num < 10:
        single_digits.append(num)
    else:
        double_digits.append(num)

print(single_digits)
print(double_digits)