#### Handling the FileNotFoundError Exception
filename = 'alice.txt' # 'save' 'file name' as a 'string' in 'variable'
try : # try to run below code - if an error occurs run code in except block
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")


## Analyzing Text 
filename = 'alice.txt' # 'save' 'file name' as a 'string' in 'variable'
try : # try to run below code - if an error occurs run code in except block
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")