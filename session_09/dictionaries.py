#!/usr/bin/env python3

# Make our first dictionary (key:value)
dict1 = {'a':0, 'b':1, 'c':2}
print(dict1)

# Mix data types in a dictionary
dict2 = {"my_string":"Coffee", "my_in":8, "my_float":9.2, "my_list":[1, 2, 3, 4, 5]}
print(dict2)

# Find values in a dictionary
dict3 = {
    "brand": "Honda",
    "model": "Civic",
    "year": 2020
}
print(dict3["brand"])

# Add new value and entry into dictionary
dict3["owner"] = "Sadie"
print(dict3)

# Delete dictionary entry
del(dict3["owner"])
print(dict3)

# Check if elements are in the dictionary (but this only works for keys not values)
check1 = "owner" in dict3
print(check1)
check2 = "year" in dict3
print(check2)
check3 = 2020 in dict3
print(check3)

# View all keys in the dictionary
print(dict3.keys())
# View all values in the dictionary
print(dict3.values())