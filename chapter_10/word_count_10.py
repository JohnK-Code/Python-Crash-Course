#### Working with Multiple Files
def count_words(filename): # 'define' function called 'count_words' with a 'paramater' called 'filename'
    """Count the approximate number of words in a file.""" # 'docstring'
    try: # try indented code
        with open(filename, encoding='utf-8') as f: # open file using 'encoding' argument - save 'file object' in 'f'
            contents = f.read() # 'read' contents of 'f' and 'save' in variable 
    except FileNotFoundError: # if this error occurs, run indented code
        print(f"Sorry, the file {filename} does not exist.") # print string - we could just put the 'pass' keyword hear so the 'try' 'fails' 'silently' and doesn't provide the user with any message 
    else: # the 'indented' code 'runs' if 'no' 'error' created from 'try block'
        words = contents.split() # 'split()' contents into a 'list' of 'words' and 'assign' to the 'variable' - default split is 'whitespace' for 'split()'
        num_words = len(words) # get the 'length' of the 'number' of 'words/values' in 'list' and 'assign' to 'num_words' variable
        print(f"The file {filename} has about {num_words} words.") # print message containing variables form above
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] # 'list' of files to be opened 'assigned' to 'variable'
for filename in filenames: # 'loop' through 'items' in variable 'list'
    count_words(filename) # 'call function' using 'variable' containing 'list item' from 'loop' 