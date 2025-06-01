requested_toppings = []
if requested_toppings: # THis will result in True as the List is currently empty and that it what it was checking for
    for requested_topping in requested_toppings:
     print("Adding " + requested_topping + ".")
     print("\nFinished making your pizza!") 
else:
    print("Are you sure you want a plain pizza?")