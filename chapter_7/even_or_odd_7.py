##### The Modulo Operator - Chapter 7
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number) # convert user input collected using the 'input()' function to an integer
if number % 2 == 0: # use the 'modulo operator' to find the remainder from the two number being divided and check 'if' it equals to '0'
    print(f"\nThe number {number} is even.") # runs 'if' condition is True
else:
    print(f"\nThe number {number} is odd.") # runs 'if' condition is False 