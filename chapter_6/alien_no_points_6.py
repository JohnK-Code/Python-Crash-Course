#### Using get() to Access Values 
alien_0 = {'color': 'green', 'speed': 'slow'} # new dict
#print(alien_0['points']) # This produces a 'KeyError' because the 'points' key doesn't exist

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.') # use 'get' method instead of square brackets to access dict values, this allows you to add a default responce incase the dict key doesn't exist instead of getting an error
print(point_value ) # 'points' key doesn't exist so the value in the 'point_value' variable will be the default value 
