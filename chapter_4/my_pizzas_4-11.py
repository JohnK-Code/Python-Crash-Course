#### TRY IT YOURSELF - My Pizza, Your Pizza
my_pizza = ["pepperoni", "magarita", "spicy chicken"]
friend_pizza = my_pizza[:]

my_pizza.append("donner")
friend_pizza.append("chicken")

print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza)

print("\n") # add new line between exercises 

print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)