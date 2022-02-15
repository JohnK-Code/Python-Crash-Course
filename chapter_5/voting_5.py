#### 'if' statements - Chapter 5
age = 19 
if age >= 18: # if greater than or equal to 18, run the indented code 
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

## 'if-else'
print("\n") # Line Break
age = 17 
if age >= 18: # the indented 'else' block will run because the if condition fails
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")