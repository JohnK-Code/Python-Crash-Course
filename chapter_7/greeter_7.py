#### Writing Clear Prompts - Chpater 7 
name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!")


#### Using a varible to store the argument for the 'input()' function - This allows the argument to cover more than one line.
print("\n") # new line
prompt = "If you tell us who you are, we can personalizze the messages you see."    # Used for the 'input()' functions arguments
prompt += "\nWhat is your first name? " # Used for the 'input()' functions arguments
name = input(prompt)
print(f"\nHello, {name.title()}") 