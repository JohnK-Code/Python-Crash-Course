#### Reading from a File - Chapter 10 - Page 184
## Reading an Entire File
# the 'open()' method can use an 'absolute' or 'relative' 'path' when specifying the files location
with open('pi_digits.txt') as file_object: # 'opens' the 'pi_digits.txt' file and 'returns' an 'object' representing this file and 'stores' it in 'file_object' - The 'with' keyword 'closes' the file once access is no longer needed, this is instead of using the 'close()' method which could lead to errors
    contents = file_object.read() # 'read' method used to read the entire contents of the 'file' and 'store' it as one long string in the 'contents' variable
print(contents.rstrip()) # 'print' the value inside the 'contents' variable - Use 'rstrip()' method to remove the 'empty string/whitespace' added at the 'right' of the 'string' by the 'read()' method 


## Reading Line by Line - Page 187
print("\n") # print a line break to seperate exercises
filename = 'pi_digits.txt' # save the name of the file to the variable 'filename'
with open(filename) as file_object2: # 'open' the 'file' and 'saves' the 'object' created to the 'variable' 'file_object2'
    for line in file_object2: # 'loop' through each 'line' in the 'file_object2' variable
        print(line.rstrip()) # print the 'line' variable - 'rstrip()' can be used to 'remove' any 'newline' characters added by the 'text file' 'pi_digits.txt' or the 'print()' method on the 'right-hand' side of the 'string' in the 'line' variable


## Making a List of Lines from a File 
print("\n") # print a line break to seperate exercises
filename2 = 'pi_digits.txt' # 'save' the name of the 'filename' to the 'variable'
with open(filename2) as file_object3: # 'open' the 'file' and 'saves' the 'object' created to the 'variable' 'file_object3'
    lines = file_object3.readlines() # 'readlines()' method takes each 'line' from the 'file' object strored in 'file_object3' and 'saves' it to a 'list' that is 'assigned' to the 'lines' variable 
for line in lines: # 'loop' through each 'item/line' in the 'lines' 'list' 
    print(line.rstrip()) # 'print()' each version of the 'line' variable until the 'loop' is finished - 'rstrip()' removes any 'whitespace' on the 'right-hand' side of the 'string' in the 'line' variable