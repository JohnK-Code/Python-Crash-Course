#### TRY IT YOURSELF - Chapter 10 - Page 202 - Addition Calculator
def addition():
    """Display the results of two numbers being added together."""
    print("Enter two numbers to be added together.")
    print("Enter 'q' to quit.")
    while True:
        num_one = input("Enter the first number: ")
        if num_one == 'q':
            print("Goodbye!")
            break
        num_two = input("Enter the second number: ")
        if num_two == 'q':
            print("Goodbye!")
            break
        try:
            num_one = int(num_one)
            num_two = int(num_two)
        except ValueError:
            print("Only numbers can be entered.\n")
        else:
            sum = num_one + num_two
            print(f"The sum of {num_one} and {num_two} is {sum}.\n")

addition()