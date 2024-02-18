# (2)
# def no_of_strings(strings):
#     count = 0
#     for i in strings:
#         if len(i) >= 2 and i[0] == i[-1]:
#             count += 1
#     return count
# sample_list = ['abc', 'xyz', 'aba', '1221']
# result = no_of_strings(sample_list)
# print("Number of strings is:", result)

#(1)
# Use dir
methods_attributes = dir(list)
print("List Methods and Attributes:", methods_attributes)

mylist = ["apple", "banana", "cherry"]
print("\nOriginal List:", mylist)
mylist.append('orange')
print("After append:", mylist)
count_banana = mylist.count('banana')
print("Count of 'banana':", count_banana)
mylist.extend(['grape', 'kiwi'])
print("After extend:", mylist)
index_cherry = mylist.index('cherry')
print("Index of 'cherry':", index_cherry)
mylist.insert(1, 'mango')
print("After insert:", mylist)
popped_item = mylist.pop(2)
print("Popped item at index 2:", popped_item)
print("After pop:", mylist)
mylist.remove('mango')
print("After remove:", mylist)
mylist.reverse()
print("After reverse:", mylist)
mylist.sort()
print("After sort:", mylist)
#using help
help_on_reverse = help(list.reverse)
print("\nHelp on reverse method:", help_on_reverse)
# Using 'reverse'
mylist.reverse()
print("After reverse:", mylist)
