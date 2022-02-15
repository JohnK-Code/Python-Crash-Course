#### TRY IT YOURSELF - Chapter 7 - Multiples of Ten
number = input("Please enter a number to see if it's a multiple of ten: ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print(f"{number} is not a multiple ten.")