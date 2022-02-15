#### TRY IT YOURSELF - Chapter 8 - T-Shirt
def make_shirt(size, message):
    """Summarize the shirt that is going to be made.""" # 'docstring'
    print(f"The size of the t-shirt is {size} and the message that will be printed is '{message}'.")
make_shirt('small', "I'm with stupid!") # call function using 'positional arguments'
make_shirt(size='small', message='Roadkill') # call function using 'keyword arguments'