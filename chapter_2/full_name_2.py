# formating strings using 'f-strings' or the older 'format()' method

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # called f-strings - replaces the variable name with it's value in the string
print(full_name)

print(f"Hello, {full_name.title()}!") # f-string from above used in a sentance and with the method 'title() that changes the first letter of each word to uppercase'

message = f"Hello, {full_name.title()}!" # assigns f-string to a variable
print(message) # prints variable with f-string as a value

full_name = "{} {}".format(first_name, last_name) # does the same as an 'f-string' but for older versions of python - basically, it replaces the curly brackets in the string with the values from the variables provided with the 'format()' method
print(full_name)
