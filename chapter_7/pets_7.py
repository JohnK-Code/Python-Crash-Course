#### Chapter 7 - Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets: # loop through the 'pets' list and remove the first occurance of the value 'cat' each time until none are left
    pets.remove('cat') # remove value 'cat' from 'pets'
print(pets) # print 'pets' list after loop finished