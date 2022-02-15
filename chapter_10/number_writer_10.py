#### Using json.dump() and json.load() - Chapter 10 - Page 203 - Number Writer
import json # 'import' 'json' 'module'

numbers = [2, 3, 5, 7, 11, 13] # assign list of numbers to varaible

filename = 'numbers.json' # 'assign' file name in 'string format' to 'variable' 
with open(filename, 'w') as f: # 'open' file in 'write' mode and 'assign' 'file object' to 'f'
    json.dump(numbers, f) # 'convert' python 'list' to 'JSON Array' to be 'saved' in opened 'file' using 'f' 'file object'