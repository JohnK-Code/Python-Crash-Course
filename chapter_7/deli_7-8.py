#### TRY IT YOURSELF - Chapter 7 - Deli
sandwich_orders = ['cheese and ham', 'philly cheesesteak', 'tuna mayo', 'coronation chicken'] # list of sandwich orders
finished_sandwiches = [] # empty list of finished sandwiches

while sandwich_orders: # loop though the 'sandwich_orders' list 'while' it still has values
    current_sandwich = sandwich_orders.pop() # remove the last value from 'sandwich_orders' and assign it to 'current_sandwich'
    print(f"I made your {current_sandwich.title()} sandwich.") # display message about current sandwich
    finished_sandwiches.append(current_sandwich) # add 'current_sandwich' to the 'finished_sandwiches' list

print("\nThe following sandwich orders have been completed:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")