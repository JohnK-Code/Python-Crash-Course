#### Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']  # new list
print(players[0:3]) # prints only the first 3 items - first, second, third - (0,1,2)

players1 = ['charles', 'martina', 'michael', 'florence', 'eli'] # new list
print(players1[1:4]) # prints only the second, third and forth items in the list - (1,2,3) 

players2 = ['charles', 'martina', 'michael', 'florence', 'eli'] # new list
print(players2[:4]) # prints the first 4 items in the list - (0,1,2,3)

players3 = ['charles', 'martina', 'michael', 'florence', 'eli'] # new list
print(players3[2:]) # prints all items from the third (2) item through to the end no matter how long the list is

players4 = ['charles', 'martina', 'michael', 'florence', 'eli'] # new list
print(players4[-3:]) # print the last three item in a list no matter the length of the list 

players5 = ['charles', 'martina', 'michael', 'florence', 'eli'] # new list
print("Here are the first three players on my team:")
for player in players4[:3]: # loop through the first three items in a list using the square brackets (slice) to specify them
    print(player.title()) # prints the first three items and capitalizs them using the 'title()' method

