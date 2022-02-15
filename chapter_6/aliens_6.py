#### Chapter 6 - Nesting
#### A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5} # dictionary 
alien_1 = {'color': 'yellow', 'points': 10} # dictionary 
alien_2 = {'color': 'red', 'points': 15} # dictionary 

aliens = [alien_0, alien_1, alien_2] # list of dictionaries

for alien in aliens:
    print(alien) # print each dictionary in the list 'aliens' 


#### Automatically create a list of 30 dictionaries using the 'range()' function
print("\n") # new line ####
aliens = [] # Make an empty list
for alien_number in range(30): # Make 30 green aliens
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]: # change the values of the first three dictionaries in the list if there 'color' is 'green'
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]: # print the first 5 dictionaries in the list 
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")