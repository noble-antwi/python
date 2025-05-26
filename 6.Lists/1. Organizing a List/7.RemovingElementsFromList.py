# Removing an Item Using the del Statement. Ths option helps to remove an item from the List at any position that you specified
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#Removing an Item Using the pop() Method
'''
The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack. In
this analogy, the top of a stack corresponds to the end of a list.
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles.pop())