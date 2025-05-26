#Removing an Item Using the pop() Method
'''
The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack. In
this analogy, the top of a stack corresponds to the end of a list.
'''
motorcycles = ['honda', 'yamaha', 'suzuki','Noble','Kokoli','Nevame']
print(motorcycles.pop()) #This will print the removed ite. NB: The item removed is the last item in the LIST
print(motorcycles)
#Popped Items can also be stored in a  variables like say
popped_motocycle = motorcycles.pop()
print(f"The last removed Item is : {popped_motocycle}")