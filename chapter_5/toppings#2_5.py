#### Testing Multiple Conditions - Chapter 5 
## Using multiple 'if' conditions because more than one could be true and we don't want the rest of the 'if' conditions skipped
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding cheese.")
print("\nFinished making your pizza!")
