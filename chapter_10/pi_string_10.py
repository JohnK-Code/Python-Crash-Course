#### Working with a File's Contents - Chapter 10 - Page 188
filename = 'pi_digits.txt' # save 'string' file name in 'variable'
with open(filename) as file_object: # 'open' 'file' and 'save' 'file object' in 'file_object' varaiable
    lines = file_object.readlines() # assign each 'line' of the 'file_object' 'string' to the 'list' 'lines'

pi_string = '' # 'empty' string 'assigned' to 'variable'
for line in lines: # 'loop' through each 'item' in the list 'lines'
    pi_string += line.strip() # 'add' each 'item' from the 'list' to the 'pi_string' variable after 'removing' all 'whitespace'  - 'strip()' removes 'whitespace' from 'strings' on both sides unlike 'rstring' or 'lstring' which remove whitespace on the specified side of the string 

print(pi_string) # 'print' contents of the 'pi_string' variable 
print(len(pi_string)) # 'print' the 'length' of the 'pi_string' variable



#### Large File: One Million Digits - Page 189-190
print("\n") # add newline between exercises
filename2 = 'pi_million_digits.txt' # save file name to variable - ##file only contains pi to 1000 digits beacause a million is to large to copy 
with open(filename2) as file_object2: # same as above exercise
    lines2 = file_object2.readlines() # same as above exercise

pi_string2 = '' # same as above exercise
for line in lines2: # same as above exercise
    pi_string2 += line.strip() # same as above exercise

print(f"{pi_string2[:50]}...") # 'prints' contents of 'pi_string2' variable up to the '50th' 'value/item'
print(len(pi_string2)) # same as above exercise



#### Is Your Birthday Contained in Pi?
birthday = input("Enter your birthday, in the form mmddyy: ") # accept 'input' form user and saves it in the variable 'birthday'
if birthday in pi_string2: # check if contents of 'birthday' is in 'pi_string2' or not 
    print("Your birthday appears in the first million (technically thousand) digits of pi!") # run if True
else:
    print("Your birthday does not appear in the first million (techinically thousand) digits of pi.") # run if False