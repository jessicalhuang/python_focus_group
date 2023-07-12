#!/usr/bin/env python3

# Create a function without arguments
def greeting():
    print("Hello, world!")
    
# Call function
greeting()


# Create a function with argument 'some_string'
def add_underscore(some_string):
    new_string = some_string + "_"
    print(new_string)

# Call function
add_underscore("Viki")


# Create a function with multiple defined arguments
def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)

# Call function
add_numbers(3, 7)


# Create a function with undefined numbers of arguments
# Add a * before the argument name in the function definition to do so
# Example: Create a function that prints the first letter initial of each input name
def first_letters(*names):
    for name in names:
        print(name[0])

first_letters("Bijoy", "Helen", "Miley", "Roxanna", "Jessica")


# Defining arguments with keywords

# Example without defining the argument
# Returns statement with "Emily" because the order of the arguments makes it so that child3 is seen as Emily
def my_kids(child3, child2, child1):
    print("The youngest child is " + child3)

my_kids("Emily", "Tobias", "Linus")

# Example with defining the argument
# Returns statement with "Linus"

my_kids(child1 = "Emily", child2 = "Tobias", child3 = "Linus")


# Setting defulat arguments in a function
# Returns "I am from USA" if no argument is entered but replaces USA with another country if entered
def my_home(country = "USA"):
    print("I am from " + country)

my_home("Sweden")
my_home("Lebanon")
my_home()


# Data types as arguments
def associate_ages(a_dictionary):
    for name, age in a_dictionary.items():
        print(f'{name} is {age} years old.')

ages = {"Viki": 25, "Logan": 25, "Osman": 30}
associate_ages(ages)

"""
# Original
print("Here, we are testing the original function")
def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)
    
my_var = add_numbers(3, 7)
print("My variable: ", my_var)
"""

# With Return - stores and uses the function output
print("Here, we are testing the rewritten function")
def add_numbers(number1, number2):
    my_sum = number1 + number2
    return my_sum

my_var = add_numbers(3, 7)
print("My variable:", my_var)


# Empty functions
# Must use pass; yields "None" if used
def empty_function():
    pass

a = empty_function()
print(a)


# Recursive functions - a function that calls on itself
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results")
tri_recursion(6)


# Create function with a description
# Helpful for helping people use created functions
def add1(a):
    """
    Add 1 to a
    """
    b = a + 1
    return b

# Execute function
add1(5)

# help(add1) - brings us to a help page (documentation string) for function add 1 that shows the information between the """