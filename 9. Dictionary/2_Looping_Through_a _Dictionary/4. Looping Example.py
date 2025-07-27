favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']

newfrieds=friends[:]
#print(type(newfrieds))

'''
friends = ['phil', 'sarah']
friends_new =[]
for new_frend in friends:
    friends_new.append(new_frend.title())
    print(f"New Frineds with Letter change is {friends_new}")
'''

for name in favorite_languages.keys():
    #print(f"Name of the current person is {name.title()}")
    if name in friends:
        print(f"Hello {name.title()}, I see your favaroute language is {favorite_languages[name].title()}")
