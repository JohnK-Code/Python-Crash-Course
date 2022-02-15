#### TRY IT YOURSELF - Chapter 7 - Movie Tickets
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished: "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print("The movie ticket is free for under 3's.")
    elif age >= 3 and age <= 12:
        print("The movie ticket is $10.")
    elif age > 12:
        print("The movie ticket is $15.")
