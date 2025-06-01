multiples=[]
for num in range(1,11):
    multiple_numbers=num*3
    multiples.append(multiple_numbers)

print(multiples)

result = [values*3 for values in range(1,11)]
print(result)