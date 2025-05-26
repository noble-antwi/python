#Link to the Question is Below:
# https://github.com/noble-antwi/automation-with-python/blob/main/Module_4/Lists/Assignments/HomeWork2.md

Invite_list=['Semebia','Mary', 'Kojo','Kafui','Jerome']


print(f"Hello {Invite_list[0]}, I am inviting you to Dinner")
print(f"Hello {Invite_list[1]}, I am inviting you to Dinner")
print(f"Hello {Invite_list[2]}, I am inviting you to Dinner")
print(f"Hello {Invite_list[3]}, I am inviting you to Dinner")
print(f"Hello {Invite_list[4]}, I am inviting you to Dinner\n\n")
#print(f"Hello {Invite_list[5]}, I am inviting you to Dinner")
#print(f"Hello {Invite_list[6]}, I am inviting you to Dinner")
print(f"Unfortunately, {Invite_list[3]}, will not be able to make it to the dinner\nI will therefore go ahead to Invite Senam\n\n")
Invite_list[3]="Senam"
print(f"Hello {Invite_list[0]}, I am inviting you to Dinner")
print(f"Hello {Invite_list[1]}, I am inviting you to Dinner")
print(f"Hello {Invite_list[2]}, I am inviting you to Dinner")
print(f"Hello {Invite_list[3]}, I am inviting you to Dinner")
print(f"Hello {Invite_list[4]}, I am inviting you to Dinner\n\n")
print("Hello Friends, I just found a Bigger Dinner table and hence will be inviting Three more people to join us\n\n")
#Use insert() to add one new guest to the beginning of your list.
Invite_list.insert(0,'Kitsi Paul Selasi')

#Use insert() to add one new guest to the middle of your list.
#print(len(Invite_list)/2)
location=int(len(Invite_list)/2) #This will however become a problem when a whole number is not obtained hence must be fixed
Invite_list.insert(location,"Totobi Kuatwi")
#Use append() to add one new guest to the end of your list.
Invite_list.append("Nana Sika")
print(Invite_list)

# Add a new line that prints a message saying that you can invite only two people for dinner.
print("Hello folks, sorry but now i can only invite two people")

popped_person = Invite_list.pop()
print(f"Hello {popped_person}, I am deeply sorry I will have to cancel your invitation due to an unforsees circumstances.")
print(Invite_list)

popped_person = Invite_list.pop()
print(f"Hello {popped_person}, I am deeply sorry I will have to cancel your invitation due to an unforsees circumstances.")
print(Invite_list)
popped_person = Invite_list.pop()
print(f"Hello {popped_person}, I am deeply sorry I will have to cancel your invitation due to an unforsees circumstances.")
print(Invite_list)
popped_person = Invite_list.pop()
print(f"Hello {popped_person}, I am deeply sorry I will have to cancel your invitation due to an unforsees circumstances.")
print(Invite_list)
popped_person = Invite_list.pop()
print(f"Hello {popped_person}, I am deeply sorry I will have to cancel your invitation due to an unforsees circumstances.")
print(Invite_list)
popped_person = Invite_list.pop()
print(f"Hello {popped_person}, I am deeply sorry I will have to cancel your invitation due to an unforsees circumstances.")
print(Invite_list)

print(f"Hello {Invite_list[0]}, I am glad to let u know that you are of the two selected for the Diner")
print(f"Hello {Invite_list[1]}, I am glad to let u know that you are of the two selected for the Diner")