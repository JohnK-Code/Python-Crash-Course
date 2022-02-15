### chapter 3 - motorcycles.py - modifying lists

motorcycles = ['honda', 'yamaha', 'suzuki'] # create list containing three values 
print(motorcycles) # print original motorcycle list 

motorcycles[0] = 'ducati' # change list value at index = from 'honda' to 'ducati'
print(motorcycles) # print motorcycle list with new value at index 0


### Adding items to the end of a list
motorcycles1 = ['honda', 'yamaha', 'suzuki'] # new list
print(motorcycles1) # print original list
motorcycles1.append('ducati') # add new element to the end of the list using the 'append' method
print(motorcycles1) # print list with new appended item at the end


### Adding items to empty list
motorcycles2 = [] # new empty list
motorcycles2.append('honda') # shows empty lists can be appended to aswell 
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2) # prints list that was originally empty with new appended values 


### Inserting items into a list
motorcycles3 = ['honda', 'yamaha', 'suzuki'] # new list
motorcycles3.insert(0, 'ducati') # insert value into list using the insert method - uses index 0
print(motorcycles3) # prints list with new inserted value 


### Removing values from a list
motorcycles4 = ['honda', 'yamaha', 'suzuki'] # new list
print(motorcycles4) # print new list 
del motorcycles4[0] # delete element at index 0 from the list 
print(motorcycles4)


### Removing a list item using the 'pop' method - this saves the removed item in a new variable
motorcycles5 = ['honda', 'yamaha', 'suzuki'] # new list 
print(motorcycles5) # print new list
popped_motorcycle = motorcycles5.pop() # removes item from list using the 'pop' method and stores it in a new variable - if 'pop' empty the last item is removed by default
print(motorcycles5) # prints original list with value removed 
print(popped_motorcycle) # prints the value removed from the end of the list 

motorcycles6 = ['honda', 'yamaha', 'suzuki'] # new list 
last_owned = motorcycles6.pop() # get last item in list - defaults to last item if empty
print(f"The last motorcycle I owned was a {last_owned.title()}.") # print string with 'last_owned' varible in it - uses f-string and 'title' method to capitalize first letter


### Popping items from any Position in a List
motorcycles7 = ['honda', 'yamaha', 'suzuki'] # new list 
first_owned = motorcycles7.pop(0) # get first item in list using 'pop' method and index 0
print(f"The first motorcycle I owned was a {first_owned.title()}.") # print string containing 'first_owned' varible using 'f-string' and 'title' method


### Remove an item by Value 
motorcycles8 = ['honda', 'yamaha', 'suzuki', 'ducati'] # new list
print(motorcycles8) # print new list - just to show it's contents before being edited
motorcycles8.remove('ducati') # remove an item form a list using the 'remove' method - the 'remove' method requires the value of the item you want to be removed to be entered between the brackets
print(motorcycles8) # print list to show item 'ducati' is no longer there

motorcycles9 = ['honda', 'yamaha', 'suzuki', 'ducati'] # new list
print(motorcycles9) # print new list 
too_expensive = 'ducati' # create a variable containing the value that is to be removed from the new list
motorcycles9.remove(too_expensive) # 'remove' item from the new list using the value specifid in the 'too_expensive' variable
print(motorcycles9) # print the edited list with the item specified in the 'too_expensive' variable removed
print(f'\nA {too_expensive.title()} is too expensive for me.') # print a string containing the value of the 'too_expensive' variable explaining why we removed the value from the list - this isn't the value removed from the list, it is the value specified in the varible although it is the same - \n is used to add a new line
# Note for 'remove' method - 'remove' method only deletes the first occurrence of the value from the list and not all of them, a loop or something similar would be required to remove them all 

