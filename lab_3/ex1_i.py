
numbers = [10,11,12,13,14,15]
square = lambda x: x ** 2
cube = lambda x: x ** 3
squares = [square(x) for x in numbers]
cubes = [cube(x) for x in numbers]
print("Numbers:", numbers)
print("Squared Numbers:", squares)
print("Cubed Numbers:", cubes)



