#### TRY IT YOURSELF - Chapter 10 - Page 201 - Addition
def addition():
    """Display the results of two numbers being added together."""
    print("Enter two numbers to be added together.")
    num_one = input("Enter the first number: ")
    num_two = input("Enter the second number: ")
    try:
        num_one = int(num_one)
        num_two = int(num_two)
    except ValueError:
        print("Only numbers can be entered.")
    else:
        sum = num_one + num_two
        print(f"The sum of {num_one} and {num_two} is {sum}.")

addition()