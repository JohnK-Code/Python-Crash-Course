#### Chapter 8 - Returning a Simple Value - Formatted Name
def get_formatted_name(first_name, last_name): # define function with two 'parameters
    """Return a full name, neatly formatted.""" # 'docstring'
    full_name = f"{first_name} {last_name}" # assign both 'parameter' values to the 'variable' 'full_name'
    return full_name.title() # return the value of the 'full_name' variable to the function call
musician = get_formatted_name('jimi', 'hendrix') # call function and save the 'returned' value to the 'musician' variable 
print(musician) # 'print' the value in the 'variable' 'musician'


#### Making an Argument Optional
## This function would only work if three 'arguments' are provided to match the three 'parameters'
print('\n\n') # new line
def get_formatted_name1(first_name, middle_name, last_name): # define a function with three 'paramaters'
    """Return a full name, neatly formatted.""" # 'docstring'
    full_name = f"{first_name} {middle_name} {last_name}" # assign 'parameter' values to the 'full_name' 'variable'
    return full_name.title() # return the value of the 'full_name' variable to the function call
musician1 = get_formatted_name1('john', 'lee', 'hooker') # call function and save the 'returned' value to the 'musician1' variable
print(musician1) # 'print' the value in the 'variable' 'musician'

## This function will work with only two and three 'arguments' because the function paramater 'middle_name' has a default value equal to an empty string
print('\n\n') # new line
def get_formatted_name2(first_name, last_name, middle_name=''): # define function with three 'parameters' - 'parameters' with 'default values' must be defined last
    """Return full name, neatly formatted."""   # 'docstring'
    if middle_name: # check 'if' 'middle_name' is 'True' and not empty - python interprets non empty strings as 'True' and empty strings as 'False'
        full_name = f"{first_name} {middle_name} {last_name}" # run this code if 'middle_name' not an empty strinf
    else:   # run below in indented code if 'middle_name' 'parameter' is an empty string 
        full_name = f"{first_name} {last_name}" # this code runs if 'middle_name' is empty string and equal to 'False'
    return full_name.title()    # 'return' 'full_name' variable value to the function call
musician2 = get_formatted_name2('jimi', 'hendrix') # call function and assign the returned value to the 'musician2' variable
print(musician2) # 'print' 'musician2' variable value
musician2 = get_formatted_name2('john', 'hooker', 'lee') # call function and assign the returned value to the 'musician2' variable
print(musician2) # 'print' 'musician2' variable value