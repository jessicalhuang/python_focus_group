# 1
my_list = ['glasses', 'canvas', 'soap', 'photo album', 5084988, 9.2, 3/11, False]
print(my_list)
print(type(my_list))

# 2
tuple_1_to_5 = tuple(range(1,6))
my_list.append(tuple_1_to_5)
print(my_list)

# 3
index_5084988 = my_list.index(5084988)
print(f'Index {index_5084988} in my_list is {my_list[index_5084988]}.')

# 4
tuple_3 = my_list[-1][2]
print(f'In my_list, index 2 of the index at the end is {tuple_3}.')

# 5
photo_album_b = my_list[3][8]
print(f'In my_list, b is found in index 8 of index 3.')

# 6
my_list_sliced = my_list[0:4]
print(my_list_sliced)

# 7
my_list.insert(4,'ideology')
print(my_list)

# 8
my_list[1] = 'panel'
print(my_list)

# 9
del(my_list[6])
print(my_list)

# 10
tuple_max = max(my_list[-1])
print(tuple_max)

# 11
numbers_1_to_20 = list(range(1,21))
print(numbers_1_to_20)