#!/usr/bin/env python3

# Examples of strings
str1 = "Hello world"
str2 = "Spring is coming!"
str3 = "My dog ate 3 slices of my pizza"
str4 = "I can't believe my dog did that"

# \n starts a new line
# \t inserts a tab
# \\ allows for putting the "\" character in a strings

# Escape Sequences
print ("Roses are red,\nViolets are blue")
print("Loading \t Done")
print("Python escape sequences use a backslash: \\")
print('I\'m in such a good mood today!')

# Can put r in front of a string to get it interpreted as a literal string
# May be useful for directory paths
print(r"//*/*//**")

# String operations
original_str = "Viki is teaching me how to code in Python"

upper_str = original_str.upper()
print(upper_str)

title_str = original_str.title()
print(title_str)

lower_str = original_str.lower()
print(lower_str)

replace_str = original_str.replace("Viki", "The internet")
print(replace_str)

# Stripping spaces
spaced_out = " M y N a m e I s J e s s i c a "
right_strip = spaced_out.rstrip()
left_strip = spaced_out.lstrip()

print(right_strip)
print(left_strip)