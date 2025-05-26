bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles[0]) #Indexing starts from 0, and hence aasking for the first item in the list.
print(bicycles[0].title())

print(f"The last element in the list is {bicycles[-1].title()}") #To access the last element in the list we make use of the -1 in the bracket

print(f"The legth or total content in the list is {len(bicycles)}")
print(f"The last element therefore can also be accessed with {bicycles[len(bicycles)-1]}")