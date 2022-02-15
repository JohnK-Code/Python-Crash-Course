#### Chapter 8 - pizza.py - Passing an Arbitrary Number of Arguments
def make_pizza(*toppings): # 'define function' using a single 'paramater' with one 'asterisk' - The single 'asterisk' tells python that it can accept multiple 'arguments' and to save them as a 'tuple' in the 'parameter' 'toppings'
    """Print the list of toppings that have been requested.""" # 'docstring'
    print(toppings) # print contents of the variable 'toppings' - The variable contains a 'tuple' because we used an 'asterisk' with the 'paramater' name, meaning it can accepts as many 'arguments' as you want and they will be stored in a 'tuple' under the 'paramater' name
make_pizza('pepperoni') # call function with one 'argument'
make_pizza('mushrooms', 'green peppers', 'extra cheese') # call function with three arguments even though the function only has one 'paramater' - This works because we use an 'asterisk' with the 'paramater' name


#### Modified version of above exercice that uses a 'for' loop to go through each topping in the 'tuple' and 'print' it seperatly
print('\n\n') # new line ##
def make_pizza1(*toppings): # define function with one 'paramater' that has a single 'asterisk' - This function will work no matter how many 'arguments' it receives because we used the 'asterisk' with the 'paramater' name
    """Summarize the pizza we are about to make.""" # 'docstring'
    print("\nMaking a pizza with the following toppings:") # print message about making pizza
    for topping in toppings: # loop through each 'topping' in the 'toppings' 'tuple'
        print(f"- {topping}") # print each 'topping'
make_pizza1('pepperoni') # call function with one 'argument' 
make_pizza1('spicy mince', 'ham', 'spicy chicken') # call the same function with three 'arguments'


#### Mixing Positional and Arbitrary Arguments
def make_pizz2(size, *toppings): # 'define' function using two 'paramaters' - 'positional' and 'keyword' 'paramaters' must be entered first before 'arbitrary' ones
    """Summarize the pizza we are about to make.""" # 'docstring'
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizz2(16, 'pepperoni')
make_pizz2(12, 'mushrooms', 'green peppers', 'extra cheese')