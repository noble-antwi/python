aliens=[]
for alien_number in range(0,30):
    new_alien = {
        'color':'green',
        'point':5,
        'speed':'slow',
    }
    aliens.append(new_alien)

#print(aliens[:5])
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['point']=10
        alien['speed']='medium'

for alien in aliens[:6]:
    print(alien)
print(f"Total number of aliens: {len(aliens)}")
