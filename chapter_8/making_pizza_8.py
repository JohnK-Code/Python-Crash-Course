#### Importing an entire module - Chapter 8 
import pizza_module_8 # open the 'pizza_module_8.py' file and copy all functions from it int this program 
pizza_module_8.make_pizza(16, 'pepperoni') # call function from the imported file using dot notation
pizza_module_8.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') # call function from the imported file using dot notation


#### Importing Specific Functions - Chapter 8
from pizza_module_8 import make_pizza # importing the 'make_pizza' function from the 'pizza_module_8' file
make_pizza(10, 'cheese', 'pepperoni') # call imported function
make_pizza(12, 'cheese', 'spicy onions', 'doner meat') # call imported function


#### Using 'as' to Give a Function an Alias
## Example - syntax for providing an alias: from 'module_name' import 'function_name' as 'fn'
from pizza_module_8 import make_pizza as mp # import the function 'make_pizza' form the 'module' pizza_module_8' and give it an alias of 'mp' using the 'as' keyword
mp(10, 'spicy chicken', 'extra cheese', 'spicy mince', 'ham') # call the 'imported' 'make_pizza' function using the 'alias' 'mp'
mp(12, 'ham', 'pineapple') # call the 'imported' 'make_pizza' function using the 'alias' 'mp'


#### Using 'as' to Give a Module an Alias 
import pizza_module_8 as p # import the 'pizza_module_8' module and give it an 'alias' of 'p' using the 'as' keyword
p.make_pizza(16, 'cheese') # call function from imported file using the alias name
p.make_pizza(12, 'extra cheese', 'pepperoni') # call function from imported file using the alias name


#### Importing All Functions in a Module 
## from 'module_name' import '*'
from pizza_module_8 import * # import all functions from module using the 'asterisk'(*) operator
make_pizza(16, 'cheese') # call function from imported module - dot notaion not required because all functions have been imported using the 'asterisk'
make_pizza(10, 'cheese', 'ham') # call function from imported module - dot notaion not required because all functions have been imported using the 'asterisk'
