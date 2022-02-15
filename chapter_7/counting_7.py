#### The While Loop in Action - Chapter 7 - counting
current_number = 1 # new variable containing a number
while current_number <= 5:  # run indented code 'while' the condition is 'True'
    print(current_number) # print variable
    current_number += 1 # add 1 to variable on each iteration of the loop


#### Using continue in a Loop
print("\n") # Line Break
current_number = 0 
while current_number < 10: # if 'current_number' 'less' than '10' run below indented code
    current_number += 1 # add one to the 'current_number' varible 
    if current_number % 2 == 0: # if number is even run below indented code
        continue    # 'continue' statement used to restart 'while' loop and ignore the rest of the code in the 'while' loop on this iteration
    print(current_number) # this code only runs if the 'if' condition above is 'False' - runs if its an 'odd' number


#### Avoiding Infinite Loops
## avoids infinate loop because 'x' is incremented by '1'
print("\n") # Line Break
x = 1
while x <= 5: # this code will only run until it reaches 5 because the 'x' variable is incremented by 1 on each iteration - This stops an infinite loop
    print(x)
    x += 1 # this stops the infinate loop by incrementing 'x' by '1' each time loops


## The below loop runs forever because the 'x' variable is not incremented on each iteration stoping it form reaching '5' 
x = 1
while x <= 5: # causes infinite loop because 'x' stays at '1'
    print(x) 