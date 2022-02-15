#### How the 'input()' Function Works
message = input("Tell me something, and I will repeat it back to you: ")    # accept user input using the 'input()' function and store it in a variable
print(message) # print varible containing the user input


#### Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:" # assigning a string to the variable 'prompt'
prompt += "\nEnter 'quit' to end the program. " # adding more to the string in the variable 'prompt'
message = "" # create 'message' variable equal to an empty string so the while loop has something to compare
while message != 'quit': # check 'message' variable not equal to 'quit' and run indented code if 'True'
    message = input(prompt)  # assign user input to the 'message' variaable
    if message != 'quit': # if 'message' variable not equal to 'quit' then run indented code
        print(message) # print contents of the 'message' variable


#### Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:" # assigning a string to the variable 'prompt'
prompt += "\nEnter 'quit' to end the program. " # adding more to the string in the variable 'prompt'
active = True # vaiable used as a 'flag' in while loop - If there is more than one condition that could make the program (while loop) stop you can just set the variable 'active' to 'False'
while active: # 'while' the variable 'active' is 'True' the indented code is run
    message = input(prompt) # the user 'input' is assigned to the variable 'message'
    if message == 'quit': # if 'message' variable equals 'quit' run indented 'if' code
        active = False
    else: # if 'message' not equal to 'quit' then run indented code below 'else'
        print(message)

