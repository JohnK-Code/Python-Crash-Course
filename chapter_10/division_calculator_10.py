#### Handling the ZeroDivisionError Exception
#print(5/0)

## Using try-except Blocks
try: # Try indented code
    print(5/0) # print contents of 'print()' method
except ZeroDivisionError: # run indented code if 'ZerDivisionError' error
    print("You can't divide by zero!") # print contents of 'print()'


## Using Exceptions to Prevent Crashes 
print("\n") # line break
print("Give me two numbers, and I'll divide them.") # print instructions
print("Enter 'q' to quit.") # print instructions
while True: # run indented code while 'True'
    first_number = input("\nFirst Number: ") # save user 'input' to 'variable' 
    if first_number == 'q': # if 'true run indented code
        break # exit 'while' loop
    second_number = input("\nSecond Number: ") # save user 'input' to 'variable'
    if second_number == 'q': # if 'True' run indented code
        break # exit 'while' loop
    answer = int(first_number) / int(second_number) # 'convert' variables as 'integers' and 'divide' them, then 'save' them to the variable
    print(answer) # 'print' variable contents


## The else Block
print("\n") # line break
print("Give me two numbers, and I'll divide them.") # print instructions
print("Enter 'q' to quit.") # print instructions
while True: # run indented code while 'True'
    first_number = input("\nFirst Number: ") # save user 'input' to 'variable' 
    if first_number == 'q': # if 'true run indented code
        break # exit 'while' loop
    second_number = input("\nSecond Number: ") # save user 'input' to 'variable'
    if second_number == 'q': # if 'True' run indented code
        break # exit 'while' loop
    try:
        answer = int(first_number) / int(second_number) # 'convert' variables as 'integers' and 'divide' them, then 'save' them to the variable
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer) # 'print' variable contents