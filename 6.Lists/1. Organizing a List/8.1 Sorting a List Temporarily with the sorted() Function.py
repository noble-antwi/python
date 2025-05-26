#if you dont want the sort to be permant but the original structure of the list should be maintained then we make use of the sorted() function

# THE SORTED FUNCTION DOES NOT SEEM TO EXIST ANY LONGER. I WILL HAVE TO RESEARCH ON THAT LATER.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"The content of the list as they are inputed are: {cars}\n *********************************************************************************")


#It is not possible to print the sort() function
cars.sort() 

#print(f"The content of the list sorted is: {cars.sorted()}\n *********************************************************************************")
cars.sort(reverse=True)
print(f"The content of the list with a reverse sort is: {cars}\n *********************************************************************************")