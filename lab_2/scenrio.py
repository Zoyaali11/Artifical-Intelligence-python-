#  set of countries
clist = {'Canada', 'USA', 'Mexico', 'Australia'}
for countries in clist:
    print(countries)

#  counts from 0 to 100
count = 0
while count <= 100:
     print(count,'\n') 
#    count += 1  

# multiplication table  
for i in range(1, 11):  
    for j in range(1, 11):   
        print(i, "*", j, "=", i * j)  

#  1 to 10 backwards
for i in reversed(range(1, 11)):  
    print(i)

#  even numbers 
n = 2  
while n <= 10:  
     print(" Even Number:", n)
     n += 2  

#  sum of numbers from 100 to 200
num = 100
result = 0 
while num <= 200:  
    result += num  
    num += 1  
print("Sum of number 100 to 200:", result)
