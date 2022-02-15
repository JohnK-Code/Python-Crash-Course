#### Using json.dump() and json.load() - Chapter 10 - Page 203 - Number Reader
import json # 'import' 'json' 'module'

filname = 'numbers.json' # 'assign' file name in 'string format' to 'variable' 
with open(filname) as f: # 'open' file in default 'read' mode and 'assign' 'file object' to 'f'
    numbers = json.load(f) # 'convert' 'JSON' data back to 'python' from 'file object' 'f' 

print(numbers) # 'print()' contents of 'numbers' variable 