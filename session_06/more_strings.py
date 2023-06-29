#!/usr/bin/env python3

# Indexing strings
string_to_index = "Index Arrays"

first_A = string_to_index[6]
print(first_A)

first_word = string_to_index[0:5]
print(first_word)

last_word = string_to_index[6:12]
print(last_word)

last_index = string_to_index[-1]
print(last_index)

# Strides
every_2nd_value = string_to_index[::2]
print(every_2nd_value)

complicated_stride = string_to_index[0:5:2]
print(complicated_stride)

# Length function
print(len(string_to_index))

# Find function
start_index_Arrays = string_to_index.find("Arrays")
print(start_index_Arrays)

not_found = string_to_index.find("I'm not here")
print(not_found)

# Replicating strings
my_bird = "Bird"
total_birds = my_bird * 3
print(total_birds)

first_name = "Jessica"
last_name = "Huang"
full_name = first_name + last_name
print(full_name)

# String formatting
print(first_name, last_name)

# 3 Methods of string formatting

txt = "Nucleus"
num = 3/11

# Method 1: printf()
print('%s %.3f' % (txt, num))
# %s indicates that the first element is a string
# %.3f means the second element is a float and 3 numbers after the decimal are displayed

print('%s %.3f %d %e' % (txt, num, 2.1, .1))

# Note: this is a very old method and is rarely used

# Method 2: str.format()

print('{} {}'.format(txt, num))
print('{} {:.3f}'.format(txt, num))

# Powerful but also ugly-looking I guess

# Method 3: f-strings
my_first_f_string = f'My first name is {first_name} and my last name is {last_name}. That makes my full name {first_name + " " + last_name}'
print(my_first_f_string)
decimal_manip = f'The value of 3/11 is {num}. If we round to three decimal places, that makes 3/11 = {num:.3f}'
print(decimal_manip)

my_variable = "variable"
print(f"Some string with my {my_variable}")
f'Some string with my {my_variable}'