#### Defining a Tuple - Tuples are like a list but can't be changed - They are Immutable 
dimensions = (200, 50) # new tuple 
print(dimensions[0]) # print the first item in a list using square brackets and index 
print(dimensions[1]) # print the second item in a list using the square brackets and index  


#### Trying to change item in a tuple - This won't work as tuples are immutable 
# dimensions[0] = 250 # Creates TypeError: 'tutple' object does not support item assignment - commented out so rest of program works


my_t = (3,) # define a tuple with one element - This isn't very common and is just shown as an example 
print(my_t)


dimensions1 = (200, 50) # new tutple
print("Original dimensions")
for dimension in dimensions1:
    print(dimension)    # print each item in a tuple using a for loop to access them 

dimensions1 = (400, 100) # You can't change items in a tuple but you can assign a new value to a variable - This is a new tuple not the same one modified
for dimension in dimensions1:
    print(dimension)    # print each item in a tuple using a for loop to access them



# Tuples are best used when you want to store a set of values that should not be changed