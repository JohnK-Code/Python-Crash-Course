#### Chapter 7 - Using 'int()' function to convert the default string created by using the 'input()' function to a number if required
height = input("How tall are you, in inches? ") # use 'input()' function to collect user input and store in variable - The 'input()' function automatically creates a string even if a number is entered
height = int(height) # convert string to an 'integer' using the 'int()' function
if height >= 48: # check if integer value now stored in the height variable is greater or equal to 48
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")