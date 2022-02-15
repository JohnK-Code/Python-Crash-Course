#### Modifying a List in a Function - Chapter 8 - Prining Models 
# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] # list 
completed_models = [] # empty list
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs: # 'while' loop that runs while the 'list' has values in it
    current_design = unprinted_designs.pop() # remove value from the end of the list 'unprinted_designs' and save it to the variable 'current_design'
    print(f"Printing model: {current_design}") # 'print' message about the current 'value' in the 'current_design' variable' 
    completed_models.append(current_design) # add variable value in 'current_design' to the end of the 'completed_models' list
# Display all completed models.
print("\nThe following models have been printed:") # 'print' message about printed models
for completed_model in completed_models: # 'loop' through 'values' in 'completed_models' list 
    print(completed_model)  # 'print' contents of the 'completed_model' variable


#### Reorganize the above code to use functions instead
print("\n\n") # new line
def print_models(unprinted_designs, completed_models): # define function with two 'paramters'
    """
    Simulate printing each design, until none are left. 
    Move each design to completed_models after printing.
    """ # 'docstring'
    while unprinted_designs: # while loop runs until there are no items left in the 'unprinted_designs' list
        current_design = unprinted_designs.pop() # remove the last value from the 'unprinted_designs' list and save it to the 'current_design' variabless
        print(f"Printing model: {current_design}") # 'print' message about the current 'value' in the 'current_design' variable' 
        completed_models.append(current_design) # add the 'value' in the 'current_design' variable to the end of the 'completed_models' list
def show_completed_models(completed_models): # define function with one 'paramater'
    """Show all the models that were printed.""" # 'docstring'
    print("\nThe following models have been printed:") # 'print' message about printed models
    for completed_model in completed_models: # loop through each 'value' in the 'completed_models' list and run indented code on the specific 'value'
        print(completed_model) # 'print' value of the 'completed_model' variable
unprinted_designs1 = ['phone case', 'robot pendant', 'dodecahedron', 'model car'] # create list with four values
completed_models1 = [] # create empty list
print_models(unprinted_designs1, completed_models1) # 'call' function and pass to 'arguments' to it
show_completed_models(completed_models1) # 'call' function and pass one 'argument' to it