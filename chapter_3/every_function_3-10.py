# TRY IT YOURSELF - Chapter 3 - Every Function
countries = ["Cuba", "USA", "New Zealand", "Australia", "Japan"] # list of countries
print(countries)

print(countries[1]) # access list value at index 1

print(countries[-1]) # access last iem in a list using '-1' - works for lists of all sizes

print(f"I would like to visit the {countries[1]} one day.") # access individual value in a list using the index number of the value - The value can be added to a string using 'f-string'

countries[3] = "Ireland" # Change the list value at index 3

countries.append("Australia") # Add item to end of list using 'append' method

countries.insert(1, "U.A.E") # add value to the list using the 'insert' method by specifying the index it should be added at and the value to be added

del countries[1] # delete item in list using the 'del' statement and specifying its list index

maybe_countries = countries.pop() # remove item from list and store in new variable - 'pop' defaults to the last item (-1) if no index value is provided 
print(maybe_countries)

countries.remove('Ireland') # remove value from list by specifying the value - a variable can also be used to specify the value 

countries.sort(reverse=True) # 'sort()' can be used to organize values alphabetically or in reverse alphabetical order using 'reverse' argument

print(sorted(countries)) # 'sorted' is used to sort the list in alphabetical or reverse alphabetical order temporarily and does not affect the original list - its results can be saved to a varible but the original list will remain the same 

countries.reverse() # 'reverse' method is used to reverse the order of the list - not alphabetically, just any order reversed

print(len(countries)) # gets the length of a list 