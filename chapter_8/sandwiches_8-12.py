#### TRY IT YOURSELF - Sandwiches - Chapter 8
def make_sandwich(*toppings):
    """Summarize the sandwich being made."""
    print("We will add the following toppings to your sandwich:")
    for topping in toppings:
        print(f"- {topping}")
    print("Your sandwich is ready.\n")

make_sandwich('cheese', 'ham', 'mustard')
make_sandwich('ham', 'pickle')
make_sandwich('bacon', 'lettuce', 'tommato', 'red sauce')