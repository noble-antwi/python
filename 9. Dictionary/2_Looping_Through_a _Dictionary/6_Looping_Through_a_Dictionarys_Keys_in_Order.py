favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in favorite_languages.keys():
    print(f"{name.title()}, thank you for taking the poll.")

print("\n")
    

for name in sorted(favorite_languages.keys()): #Puts the names in alphabetical order
    # The sorted() function sorts the keys in alphabetical order
    # and returns a new list of the sorted keys.
    # This does not change the original dictionary.
    print(f"{name.title()}, thank you for taking the poll.")


#print(sorted(favorite_languages)) #This will print the keys in alphabetical order