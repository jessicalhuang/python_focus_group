#!/usr/bin/env python3

tuple1 = ("disco", 10, 1.2)
print(type(tuple1))

# Indexing tuples
first_element = tuple1[0]
first_el_type = type(tuple1[0])
print(first_element, first_el_type)

# Using negative indexing
last = tuple1[-1]
second_to_last = tuple1[-2]
third_to_last = tuple1[-3]
print(f'The last element is {last}. The second to last element is {second_to_last}. The third to last (first in this case) element is {third_to_last}')

# Find element index
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")
disco_tuple = genres_tuple.index("disco")
rock_tuple = genres_tuple.index("rock")
print(disco_tuple)
print(rock_tuple)

# Slicing tuples
tuple_to_slice = ("disco", 10, 1.2, "hard rock", 10)
print(tuple_to_slice[0:3])

# Determine length of tuple
print(len(tuple_to_slice))

# Use the sorted() function
Ratings = (10, 9, 6, 7, 10, 8, 9, 6, 2)
print(f'The original tuple is: {Ratings}')

Ratings_Sorted = sorted(Ratings)
print(f'The sorted tuple is: {Ratings_Sorted}. Notice that our original tuple, {Ratings} is still unsorted')

print(type(Ratings))
print(type(Ratings_Sorted))

# Sort tuples with strings
Cars = ("bmx", "audi", "toyota", "subaru")
Cars_sorted = sorted(Cars)
print(Cars_sorted)

# Concatenating tuples
tuple1 = ("disco", 10, 1.2)
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

# Work with nested tuples
nested_tuple = (1, 2, ("pop", "rock"), (3, 4), ("disco", (5, 6)))

# Access the nested tuple at index 2
print(nested_tuple[2])

# Access the first element of the nested tuple at index 2 ("pop")
print(nested_tuple[2][0])

# Access the double nested 6 at the very end of the tuple
print(nested_tuple[4][1][1])

# Access the "s" in "disco"
print(nested_tuple[4][0][2])