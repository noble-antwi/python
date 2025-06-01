my_foods = ['pizza', 'falafel', 'carrot cake']

new_my_food  = my_foods[:] # This copies the original list into the new list variable name of
#new_my_food
my_foods.append("Hello Word")
new_my_food.append("Waakye")

print(f"{new_my_food}\n")
print(f"{my_foods}\n")

my_foods=new_my_food
#The above ensures whatever that is added ot my_foods also get populated to new_my_foods
my_foods.append("Jollof Rice")

print(f"{new_my_food}\n")