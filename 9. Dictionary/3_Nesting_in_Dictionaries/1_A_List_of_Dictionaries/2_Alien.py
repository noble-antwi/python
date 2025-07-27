content =[]

for num in range(30):
    alien = {
        'color': 'green',
        'point': 45,
        'height': '70m',
        'weight': '80kg',
        'origin': 'Space World'
    }
    content.append(alien)

#print("Printing the content of the list of dictionaries, and they are below: \n", content)

for new in content[:3]:
    print(new)

