#### Chapter 8 - Greet Users - Passing a List
def greet_users(names): # define function with one 'paramater'
    """Print a simple greeting to each user in the list.""" # 'docstring'
    for name in names: # loop through 'values' in 'names' 'list' 
        msg = f"Hello, {name.title()}!" # variable 'msg' is assigned a string containing a message with a 'value' from the 'list'
        print(msg) # print 'msg' variable contents 
username = ['hannah', 'ty', 'margot'] # assign 'list' of 'values' to 'variable' 'username'
greet_users(username) # 'call' function with 'username' variable as an 'argument