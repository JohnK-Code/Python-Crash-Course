#### Chapter 6 - Alien - Dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


#### Accessing Values in a Dictionary 
alien_0 = {"color": "green"} # simple ductionary with one key value pair
print(alien_0["color"]) # accessing the value 'green' by providing the dictionary name and the key value in square brackets


#### Accessing the points for an alien that is shot 
print("\n") # New line
alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"] # assigning the value of the key 'points' in the dictionary 'alien_0' to the variable 'new_points' - The value is '5'
print(f"You just earned {new_points} points!") # Print a string telling the user they earned '5' points by adding the value from the variable 'new_points' to the string


#### Adding new key-value pairs
print("\n") # new line
alien_0 = {"color": "green", "points": "5"} # new dictionary
print(alien_0) # print dictionary 
alien_0['x_position'] = 0 # add new key-value pair to the 'alien_0' dictionary
alien_0['y_position'] = 25 # add new key-value pair to the 'alien_0' dictionary
print(alien_0) # print 'alien_0' dictionary with new key-value pairs


#### Starting with an empty dictionary
print("\n") # new line 
alien_0 = {} # new dictionary
alien_0["color"] = "green" # add key-value pair to empty dictionary 
alien_0["points"] = 5 # add key-value pair to dictionary
print(alien_0) # print modified dictionary 


#### Modifying Values in a Dictionary 
print("\n") # new line
alien_0 = {"color": "green"} # new dictionary
print(f"The alien is {alien_0['color']}.") # print string containing the value of the key 'color' in the dictionary 'alien_0'
alien_0['color'] = 'yellow' # change the value associated to the key 'color' in the dictionary 'alien_0'
print(f"The alien is now {alien_0['color']}.") # print string containing the new value associated with the key 'color' in the dict 'alien_0'

## Move Alien 
print("\n") # new line
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"} # new dict
print(f"Original position: {alien_0['x_position']}") # print string containing the original value for the key 'x_position'
# Move alien to the right.
# Determine how far to move the alien based on it's current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3
# The new position is the old position plus the increment
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']}")


#### Removing Key-Value pairs
print("\n") # new line
alien_0 = {"color": "green", "points": 5} # new dict
print(alien_0) # print new dict 
del alien_0["points"] # delete the key 'points' and it's associated value from the dict 'alien_0' - (note) be aware this deletes key-value pair permanently 
print(alien_0) # print the modified dict to show the delete worked


#### A Dictionary of Similar Objects 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }