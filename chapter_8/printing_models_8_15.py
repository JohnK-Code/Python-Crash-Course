#### TRY IT YOURSELF - Chapter 8 - Printing Models 
## Other code from the file 'printing_models_8.py' file that calls the function that is now in a module
import printing_functions_8_15
from printing_functions_8_15 import print_models

unprinted_designs1 = ['phone case', 'robot pendant', 'dodecahedron', 'model car'] # create list with four values
completed_models1 = [] # create empty list
printing_functions_8_15.print_models(unprinted_designs1, completed_models1)
printing_functions_8_15.show_completed_models(completed_models1)
