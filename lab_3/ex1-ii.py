starts_with = lambda s, c: s[0] == c
s = input("Enter a string: ")
c = input("Enter a character: ")
result = starts_with(s, c)
if result:
    print(f"The string '{s}' starts with the character '{c}'.")
else:
    print(f"The string '{s}' does not start with the character '{c}'.")
