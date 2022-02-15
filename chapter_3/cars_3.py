### Chapter 3 - Organizing a list - Cars - Sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru'] # new list 
cars.sort() # sorts the list alphabetically
print(cars)
cars.sort(reverse=True) # sort the list in reverse alphabetical order
print(cars)
print("\n") # just adds a new line between exercises - nothing to do with exersise


### Sorting a List Temporarily with the sorted() Function
cars1 = ['bmw', 'audi', 'toyota', 'subaru'] # new list
print("Here is the original list:")
print(cars1) # print original list
print("\nHere is the sorted list:")
print(sorted(cars1)) # create a temporary sorted list from the cars list provided
print("\nHere is the original list again:")
print(cars1) # print original list again to show that the 'sorted()' function did not change it
print("\n") # just adds a new line between exercises - nothing to do with exersise


### Printing a List in Reverse Order 
cars2 = ['bmw', 'audi', 'toyota', 'subaru'] # new list
print(cars2) # print new list
cars2.reverse() # revereses the order of the list permanently but not alphabetically - just reverses the list order
print(cars2)
print("\n") # just adds a new line between exercises - nothing to do with exersise


### Finding the Length of a List
cars3 = ['bmw', 'audi', 'toyota', 'subaru'] # new list
print(len(cars3))