#### Refactoring - Chapter 10 - Page 206 
## code from 'remember_me_2_10.py' refactored into functions to improve it usefullness 
import json

def get_stored_username(): # define function
    """Get stored username iis available.""" # 'docstring'
    filename = 'username.json' # assign 'filename' as a 'string' to the 'variable'
    try: # try indented code 
        with open(filename) as f: # 'open file' in 'read mode' (default) and 'save' 'file object' to 'f'
            username = json.load(f) # 'convert json' back to 'python' from 'open' file and 'assign' to 'variable'
    except FileNotFoundError: # 'run' indented 'code' if 'try' code produces specified 'error'
        return None # return None
    else: # if 'try' succesfull, run indented code
        return username # return varaible 

def get_new_username(): # define function
    """Prompt for a new username.""" # 'docstring'
    username = input("What is your name? ") # assign user input to variable
    filename = 'username.json' # assign 'filename' as a 'string' to the 'variable'
    with open(filename, 'w') as f: # 'open file' in 'write mode' and 'save' 'file object' to 'f'
        json.dump(username, f) # 'convert' user input in 'username' variable to 'json' and 'save' to 'file' assigned to 'f'
    return username

def greet_user(): # define function
    """Greet the user by name.""" # 'docstring'
    username = get_stored_username() # 'call' function and 'assign' responce back to 'varaiable'
    if username: # if variable exists/True run indented code
        print(f"Welcome back, {username}!") # print message containing variable
    else: # run indented code if 'username' variable doesn't exist/False
            username = get_new_username() # call function to get new username and assign returned data to variable
            print(f"We'll remember you when you come back, {username}!") # print message containing variable


greet_user() # call function