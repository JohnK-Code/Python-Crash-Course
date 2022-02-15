#### Chapter 8 - Greeter - Defining a Function
def greet_user():   # define the 'greet_user()' function
    """Display a simple greeting."""    # 'docstring' - like a comment that is used by python to generate documentation about the function
    print("Hello!")  # 'print' string when function called
greet_user()    # function call - This is used to run the function 


#### Passing Information to a Function
def greet_user1(username): # define the 'greet_user1()' function - This function has a 'paramater' called 'username' that accepts an 'argument' from the function call 
    """Display a simple greeting."""    # 'docstring' used for python documentation
    print(f"Hello, {username.title()}!")    # 'prints' string containing the 'paramater/argument' being passed into the function when called - 'username'
greet_user1("john") # function call - Used to run the function - This call also has an 'argument' it provides to the function - the 'argument' 'john' is assigned to the paramater 'username' that can be used in the function


#### Using a Funtion with a while loop - infinate loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# This is an infinate loop!
#while True:    # remove this comment to run this loop ####################
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


#### Using a function with a while loop but this time the user can exit by entering 'q'
def get_formatted_name1(first_name, last_name): # define function
    """Retrun a full name, neatly formatted.""" # 'docstring'
    full_name = f"{first_name} {last_name}" # save 'paramater' values in a string wihtin the variable 'full_name'
    return full_name.title() # 'return' 'full_name' variable to the function 'call' 
while True: # run loop 'while' 'True'
    print("\nPlease tell me your name:") # print string
    print("(enter 'q' at any time to quit)") # print string 
    f_name = input("First name: ")  # save user 'input' to variable 'f_name'
    if f_name == 'q': # check 'if' 'f_name' is equal to 'q' - if True run below indented code
        break # exit while loop
    l_name = input("Last name: ") # save user input to 'l_name' variable 
    if l_name == 'q': # check 'if' 'l_name' is equal to 'q' - if True run below indented code
        break   # exit while loop
    formatted_name = get_formatted_name1(f_name, l_name) # 'call' function and save returned data to the variable 'formatted_name'
    print(f"\nHello, {formatted_name}!")
