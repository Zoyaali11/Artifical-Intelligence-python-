# Yes, a for loop can be used inside a while loop.
count = 0
while count< 2:
    for i in range(2):
        print(i)
    count += 1
