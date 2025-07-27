alien={'color':'green',
       'point':45,
       'height':'70m',
       'weight':'80kg'
       }

for identity in alien.keys():
    print(identity.title())


# Looping through keys is actually the default behaviour of looking in Dictionary and hence you may not need to add the .keys method.
print('------------------------------------------------------------\nWithout the use of .key method\n------------------------------------------------------------')
for identity in alien:
    print(identity.title())