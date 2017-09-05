# List - Example creating lists and nesting lists within lists.
# Also for loops for a specific item in the list
# Lists are SEQUENCE bases...0 1 2 3 etc...the spots they hold

print("\n\n---Lists---\n")
list_1 = [1, 2, 3]

print(list_1)

list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

matrix = [list_1, list_2, list_3]

print(matrix)

print(matrix[0][2])

first_col = [item[2] for item in matrix]
print(first_col)



# Dictionaries
# Dicts are mappings or key value pairs NOT sequence necessarily
print("\n\n\n---Dictionaries---\n")

my_dict = {'name1': 'dan', 'name2': 'john', 'name3': 'bob'}
my_dict_input = {'key1': 'value'}
print(my_dict_input)

print(my_dict_input['key1'])

print(my_dict.keys())
print(my_dict.values())

print(my_dict_input.items())
print(my_dict.items())

print(my_dict['name2'])


print('\n\n\n---Tuples---\n')



print('reading files')

file = open('test.txt')
print(file.read())

#this will fail as the file is read and python is at the end of the sentence, use seek to reset to 0 point
print(file.read())

file.seek(0)

print(file.read())






















