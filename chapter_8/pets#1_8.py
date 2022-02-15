#### Chapter 8 - Keyword Arguments - This allows you to assign the 'arguments' in the function call using a 'key' 'value' with the 'key' refering to the name of the required 'paramater' in the function definition and the 'value' being equal to the 'argument' in the call - This means the 'argument' order doesn't matter now
## Explicitly tell python which 'paramater' each 'argument' should be assigned to 
def describe_pets(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pets(animal_type='hamster', pet_name='harry') # call function 'describe_pets' using 'key' 'value' pairs, this means the order no longer mattter, unlike in 'positional arguments' where it does
describe_pets(pet_name='harry', animal_type='hamster') # 'argument' order doesn't matter when using 'keyword arguments' - This produces the same result as the above 'function call'


#### Default Values - a default 'argument' value is provided in the function definition with the 'paramater' and is only used if an 'argument' isn't provided for the 'paramater' in the function call 
## Function that have 'paramaters' wuth default values should define the ones with 'default values' last - This allows python to use 'positional arguments' correctly 
def describe_pets1(pet_name, animal_type='dog'): # define function - default value ('argument') is prvided for the 'animal_type' 'paramater' and will be used if a corresponding 'argument' isn't provided in the function call - The paramater order has been changed so that first 'paramater' is 'pet_name' meaning that the function call only needs to specify the required 'argument' and doesn't have to mention the one with a default value if you don't want to.
    """Display info about a pet.""" # 'docstring'
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pets1(pet_name='willie') # call function - only the 'argument' corresponding to the 'pet_name' 'paramater' is provided so the default one for the 'animal_type' in the function definition is used
describe_pets(pet_name='harry', animal_type='hamster') # function call - Because an 'argument' has been specified for the 'animal_type' 'paramater' the defauly one 'animal_type=dog' from the function definition will be ignored 


#### Equivalent Function Calls - Chapter 8 - Positional arguments, keyword arguments, and default values can all be used together if you want
## All the below 'function calls' would work for the function 'describe_pets1()'
# A dog named Willie
describe_pets1('willie')
describe_pets1(pet_name='willie')
# A hamster named Harry
describe_pets1('harry', 'hamster')
describe_pets1(pet_name='harry', animal_type='hamster')
describe_pets1(animal_type='hamster', pet_name='harry')


#### Avoiding Argument Errors - Make sure you provide the correct amount of 'arguments' for the function
def describe_pets2(animal_type, pet_name):
    """Display info about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pets2() # This would cause an error because no 'arguments' have been provided for 'describe_pets2' when it requires 2
