# s = 'abc'
# capitalized = s.capitalize()
# print("capitalize:", capitalized)
#
# centered_string = s.center(10, '*')
# print("center:", centered_string)
# count_char = s.count('a')
# print("count:", count_char)
# encoded_bytes = s.encode(encoding='utf-8')
# print("encode:", encoded_bytes)
#
# ends_with_c = s.endswith('c')
# print("endswith:", ends_with_c)
#
# index_of_c = s.find('c')
# print("find:", index_of_c)
#
# lowercased = s.lower()
# print("lower:", lowercased)
#
# replaced = s.replace('a', 'v')
# print("replace:", replaced)
# result= s.split('b')
# print("split:", result)
# uppercased = s.upper()
# print("upper:", uppercased)

# >> help(s.find)

# Define a string
# Define a string
s = 'abc'
help_find=help(s.find)

# Print docstring for the find method
print("Help on find method:", help_find)

# Use the find method to locate the substring 'b' in the string
result_of_find = s.find('b')
print("Index of 'b' in the string:", result_of_find)



