#### TRY IT YOURSELF - Chapter 7 - Pizza Toppings 
prompt = "\nWhat topping do you want on your pizza?"
prompt += "\nEnter 'quit' when you are finished adding toppings: "
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"  We will add {topping.title()} to your pizza.")