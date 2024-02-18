
file = open('cities.txt', 'w')
num_cities = int(input("Enter the number of cities: "))
for _ in range(num_cities):
    name = input("Enter city name: ")
    file.write(name + '\n')
file.close()

print("City names have been stored in cities.txt")
