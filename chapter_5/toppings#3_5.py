#### Toppings - Chapter 5 - Checking for Special Items
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings: # prints below string for each list item
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


print("\n") # new line
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings: # loops through each list item
    if requested_topping == "green peppers": # Checks if list contains 'green peppers' and prints the appropriate string if it is or isn't
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


### Checking That a List is Not Empty
print("\n") # New Line
requested_toppings = []
if requested_toppings: # False if list empty and True if list has values 
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


### Using Multiple Lists
print("\n") # new line
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings: # loop through 'requested_toppings'
    if requested_topping in available_toppings: # run indented code if condition 'True'
        print(f"Adding {requested_topping}.")
    else:                                       # run indented code if above condition 'False'
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making pizza!")   # Runs no matter what because it isn't inside above 'for' and 'if' code 