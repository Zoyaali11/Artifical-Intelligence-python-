def convert(num):
    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    roman = ''
    i = 0
    while num > 0:
        while num >= vals[i]:
            roman += symbol[i]
            num -= vals[i]
        i += 1
    
    return roman

num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    roman = convert(num)
    print("Roman numeral:", roman)
