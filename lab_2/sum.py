# Yes, we can sum number in a while loop.
sum = 0
count = 1

while count <= 2:
    number = int(input("Enter a number: "))
    sum += number
    count += 1

print("The sum of the numbers is:", sum)