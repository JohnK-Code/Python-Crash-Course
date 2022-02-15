#### TRY IT YOURSELF - Chapter 8 - Large Shirts
def make_shirt(size='large', message='I love Python'):
    """Summarize the shirt that is going to be made.""" # 'docstring'
    print(f"The size of the t-shirt is {size} and the message that will be printed is '{message}'.")
make_shirt() # call function with no 'arguments' so that it uses the default 'paramaters' defined in the function
make_shirt('medium') # call function and provide the 'size' argument but use the 'default value' for the 'message' 'paramater'
make_shirt('small', 'King John') # call function but this time provide both 'arguments' so that the 'default values' aren't used
