#### squares
squares = []    # New empty list
for value in range(1, 11):  # Uses the range function to provide values 1 to 10
    square = value ** 2 # Uses 'exponent' operator '**' to get the second power of the 'value' varaible
    squares.append(square) # Appends the 'square' value to the 'squares' list
print(squares)

squares1 = []   # new empty list
for value in range(1, 11):
    squares1.append(value ** 2) # Same as above but without the need for the 'square' variable - Appends value straight to list without variable 
print(squares1)


#### Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # new list of numbers
print(min(digits))  # 'min' function finds smallest number in iterable 
print(max(digits))  # 'max' function finds largest number in iterable 
print(sum(digits))  # 'sum' function gets the value of all digits added together in iterable 


#### List Comprehensions
squares2 = [value**2 for value in range(1, 11)] # Uses list comprehension to get the second power of the 'value' variable in the 'range' function
print(squares2)
