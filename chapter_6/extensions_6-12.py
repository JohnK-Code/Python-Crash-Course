#### TRY IT YOURSELF - Chapter 6 - Extensions
# Editing one of the previous programs to make it more complex - 'pizza_6.py'
# Old Code
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
        "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")


#### New Code - updated 'pizza_6.py' program
pizza_orders = {
    'order_1': {
        'crust': ['thick'],
        'toppings': ['pepperoni', 'mozzarella', 'spicy mince'],
        'size': ['10"'],
    },
    'order_2': {
        'crust': ['stonebaked'],
        'toppings': ['spicy chicken', 'peppers', 'ham'],
        'size': ['12"'],
    },
    'order_3': {
        'crust': ['deep dish'],
        'toppings': ['pepperoni', 'cheese', 'spicy mince'],
        'size': ['10"'],
    }
}
for order_num, details in pizza_orders.items():
    print(f"\n{order_num.upper()}: ")
    for pizza_spec_name, pizza_specs in details.items():
        print(f"\t{pizza_spec_name.title()} Requested:") 
        for pizza_spec in pizza_specs:
            print(f"\t\t-{pizza_spec.title()}")