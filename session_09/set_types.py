#!/usr/bin/env python3

# Sets are a collection like lists and tuples, but they do not record element position and so cannot be indexed.
# Defined using {} like dictionaries, but without the key:values

# Creating a set using list-to-set type-casting
album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)

# Add an element to the set
album_set.add("Back in Black")
print(album_set)

# Remove an element from the set
album_set.remove(10.0)
print(album_set)

# Verify element presence in a list
exists = "Back in Black" in album_set
print(exists)

no_exists = "Pillow" in album_set
print(no_exists)

# Find intersecting elements in sets
another_album_set = {"Thriller", "Closer", "The Queen is Dead", "Born in the USA", "Synchronicity"}
my_intersections1 = album_set & another_album_set
print(my_intersections1)

my_intersections2 = album_set.intersection(another_album_set)
print(my_intersections2)

# Find elements unique to each set
unique_to_album_set = album_set.difference(another_album_set)
unique_to_another_album_set = another_album_set.difference(album_set)
print(f'My album_set is {album_set} and another_album_set is {another_album_set}. {unique_to_album_set} are unique to album_set and {unique_to_another_album_set} are unique to another_album_set')

# Combine sets
# Sets only contain unique terms, so terms that were in both lists will not be duplicated - i.e. Thriller will only appear once here
combined_sets = album_set.union(another_album_set)
print(combined_sets)

# Demonstrate lack of duplicates in sets
duplicated_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(duplicated_list)

duplicated_list_as_set = set(duplicated_list)
print(duplicated_list_as_set)

# Supersets and subsets
my_subset = {'A', 'B', 'C'}
my_superset = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}

# Check if a set is a superset
check_superset1 = my_superset.issuperset(my_subset)
print(check_superset1)
check_superset2 = my_subset.issuperset(my_superset)
print(check_superset2)

# Check if a set is a subset
check_subset1 = my_superset.issubset(my_subset)
print(check_subset1)
check_subset2 = my_subset.issubset(my_superset)
print(check_subset2)

# Frozen sets: immutable version of a set (can't be edited)
# Can be used as keys in dictionaries or elements in another set
# Make an empty frozen set
print(f'The empty frozen set is: {frozenset()}')

# Tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
# Turn the tuple of vowels into a frozenset
fSet = frozenset(vowels)
print(f'The frozen set is: {fSet}')

# Frozen sets are immutable - cannot add stuff to it
# fSet.add('v') returns an AttributeError: 'frozenset' object has no attribute 'add'

# Random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
# Turn dictionary keys into a frozen set
fSet = frozenset(person)
print(f'The frozen set is: {fSet}')