#### Saving and Reading User-Generated Data - Chapter 10 - Page 204 
# exercise 'remember_me_10.py' and 'greet_user.py' combined for same exercise - shows they work better together than seperate
import json  # import json module

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json' # assign 'filename' as a 'string' to the 'variable'
try: # try indented code 
    with open(filename) as f: # 'open file' in 'read mode' (default) and 'save' 'file object' to 'f'
        username = json.load(f) # 'convert json' back to 'python' from 'open' file and 'assign' to 'variable'
except FileNotFoundError: # 'run' indented 'code' if 'try' code produces specified 'error' 
    username = input("What is your name? ") # assign user input to variable
    with open(filename, 'w') as f: # 'open file' in 'write mode' and 'save' 'file object' to 'f'
        json.dump(username, f) # 'convert' user input in 'username' variable to 'json' and 'save' to 'file' assigned to 'f'
        print(f"We'll remember you when you come back, {username}!") # print message containing variable
else: # run indented code if try block is successfull
    print(f"Welcome back, {username}") # print message 