# # 1
# vegetables = ['CARROT', 'TOMATO', 'Broccoli', 'Spinach', 'Cucumber', 'Potato', 'Zucchini']
# lowercase = [veg.lower() for veg in vegetables if len(veg) > 5]
# print("Lowercased veg with length greater than five:", lowercase, end="\n")



#  2
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
remove_element = [0, 4, 5]
new_list = []
index = 0
for value in sample_list:
    if index not in remove_element:
        new_list.append(value)
    index += 1  #  increment the index

print("List after removing elements:", new_list)
