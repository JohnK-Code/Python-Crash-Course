#### Chapter 8 - pets - Positional Arguments - Python works through the arguments you provide when calling the function and matches each one with the corresponding paramater in the funtion definition.

def describe_pet(animal_type, pet_name): # defining function - Positional Arguments - 'paramaters' match the order of the 'arguments' from the function call 
    """Display info about a pet.""" # 'docstring' 
    print(f"\nI have a {animal_type}.") # 'print' string containing the 'paramter' 'animal_type' value
    print(f"My {animal_type}'s name is {pet_name.title()}.")    # 'print' string containing the 'paramter' 'animal_type' and 'pet_name' values
describe_pet("hamster", 'harry') # 'call' function using 'positional arguments' - 'arguments' are assigned in the same order as 'paramaters' in the function definition


#### Multiple Function Calls 
def describe_pet1(animal_type, pet_name): # define function 
    """Display info about a pet.""" # 'docstring'
    print(f"\nI have a {animal_type}.") # print string containing function 'paramater'
    print(f"My {animal_type}'s name is {pet_name.title()}.") # print string containing both function 'paramaters'
describe_pet1('cat', 'cliff') # call function and provide 'positionl arguments' - The function can be called as many times as needed
describe_pet1('dog', 'vinny')    # call function and provide 'positionl arguments' - The function can be called as many times as needed


#### Order Matters in Positional Arguments 
def describe_pet2(animal_type, pet_name):
    """Display info about a pet.""" # 'docstring'
    print(f"\nI have a {animal_type}.") # print string containing function 'paramater'
    print(f"My {animal_type}'s name is {pet_name.title()}.") # print string containing both function 'paramaters'
describe_pet2("harry", "hamster") # function 'called' but 'arguments' have been provided in the wrong order causing the wrong 'value' to be assigned to the wrong 'paramater' --- 'harry' = 'animal_type' & 'hamster' = 'pet_name'
