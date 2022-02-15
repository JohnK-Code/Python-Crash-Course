#### Saving and Reading User-Generated Data - Chapter 10 - Page 204 
import json # import json module

username = input("What is your name? ") # assign user input to variable

filename = 'username.json' # 'assign' 'file name' as a 'string' to the 'varaiable'ss
with open(filename, 'w') as f: # open file 'filename' in 'write' mode and assign the 'file object' to 'f'
    json.dump(username, f) # convert the 'username' variable to 'json' and save in the 'file object' assigned to 'f' 
    print(f"We'll remember you when you come back, {username}!") # 'print()' message 