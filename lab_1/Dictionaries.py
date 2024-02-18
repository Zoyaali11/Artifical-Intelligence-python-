# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# result = {}
# result.update(dic1)
# result.update(dic2)
# result.update(dic3)
# print("Dictionary:", result)
# Creating a dictionary
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}
methods_attributes = dir(country_capitals)
print("Methods and Attributes for dictionaries:", methods_attributes)
help_method = help(country_capitals.get)
print("\nHelp on get method:", help_method)
result = country_capitals.get('Canada')
print("\nResult of using method:", result)


