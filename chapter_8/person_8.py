#### Returning a Dictionary - Chapter 8 - Person
def build_person(first_name, last_name): # define function with two 'parameters'
    """Return a dictionary of info about a person.""" # 'docstring'
    person = {'first': first_name, 'last': last_name} # save 'paramaters' as 'dictionary' 'values'
    return person   # 'return' 'variable' containing 'dictionary' to the 'function call'
musician = build_person('jimi', 'hendrix') # 'call' function and save 'return' data to the 'musician' variable
print(musician) # 'print' 'variable' containing 'dictionary' 'returned' from function


#### Same function but this time with an optional 'paramater' called 'age'
def build_person1(first_name, last_name, age=None): # define function with three 'parameters' with the last having a 'default value' of 'None'
    """Return a dictionary of info about a person.""" # 'docstring'
    person = {'first': first_name, 'last': last_name} # save 'paramater' values to a 'dictionary' in the variable 'person'
    if age: # check 'if' age 'True' - This is 'True' 'if' an 'argument' is prvided for this paramater
        person['age'] = age # add 'age' 'parameter' to 'person' 'dictionary'
    return person # return 'person' variable to function 'call'
musician = build_person1('jimi', 'hendrix', age=27) # 'call' function with provided 'arguments' and save returned data to the 'variable' 'musician'
print(musician) # print 'musician' vairable