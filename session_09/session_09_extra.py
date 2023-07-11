# 1
my_dict = {"confusion": True, "recording": "No", "organization": 57, "complaints": [1,2,3], "soup": "alphabet"}
print(my_dict)

# 2
print(my_dict["recording"])

# 3
my_dict["catastrophe"] = False
print(my_dict)

# 4
del(my_dict["recording"])
print(my_dict)

# 5
print("soup" in my_dict)

# 6
print(my_dict.keys())

# 7
print(my_dict.values())

# 8
my_list = ['Balalaika', 'Bouqet', 'Outlook', 'Petticoat', 'Summit', 'Chime', 'Labourer', 'Patty', 'Persimmon', 'Sample']
print(my_list)

# 9
my_set1 = set(my_list)
print(my_set1)

# 10
my_set1.add('Nucleotidase')
print(my_set1)

# 11
my_set1.remove('Summit')
print(my_set1)

# 12
print('Violin' in my_set1)

# 13
my_set2 = {'Alias', 'Assist', 'Belfry', 'Sideboard', 'Soap', 'Balalaika', 'Persimmon'}
print(my_set2)

# 14
intersect1 = my_set1 & my_set2
print(intersect1)

# 15
unique_my_set2 = my_set2.difference(my_set1)
print(unique_my_set2)

# 16
combined_sets = my_set1.union(my_set2)
print(combined_sets)

# 17
a = 16653509
b = 2448111
print(a == b)

# 18
if a > b:
    print('a is greater than b')
if b > a:
    print('b is greater than a')