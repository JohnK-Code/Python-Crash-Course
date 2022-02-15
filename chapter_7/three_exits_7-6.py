#### TRY IT YOURSELF - Chapter 7 - Three Exits

## Redo Exercise pizza_toppings_7-4.py but with the 'break' statement
prompt = "\nWhat topping do you want on your pizza?"
prompt += "\nEnter 'quit' when you are finished adding toppings: "
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"  We will add {topping.title()} to your pizza.")


## Redo Exercise movie_tckets_7-5.py but using a 'flag'
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished: "
active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("The movie ticket is free for under 3's.")
        elif age >= 3 and age <= 12:
            print("The movie ticket is $10.")
        elif age > 12:
            print("The movie ticket is $15.")


## Redo exercice pizz_toppings_7-4.py but with a 'condition' in the 'while' loop
prompt = "\nWhat topping do you want on your pizza?"
prompt += "\nEnter each one seperatly. You are allowed a total of 3: "
num = 1
while num <= 3:
    topping = input(prompt)    
    print(f"  We will add {topping.title()} to your pizza.")
    num += 1