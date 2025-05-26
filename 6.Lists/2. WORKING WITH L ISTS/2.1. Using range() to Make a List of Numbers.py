'''If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function. When you wrap list() around a
call to the range() function, the output will be a list of numbers.'''
numbers= list(range(1,13))
print(numbers)


'''We can also use the range() function to tell Python to skip numbers
in a given range.'''

even_numbers = list(range(2,24,2))
print(even_numbers)

#MAKING SQUARES OF NUMBERS

square_set=[]

for number in range(1,15):
    square=number**2
    square_set.append(square)
    print(f"The square of {number} is {square}")

print(f"The total squares are: {square_set}")

