#### Chapter 4 - magicians - looping through an entire list
magicians = ["alice", "david", "carolina"] # new list 
for magician in magicians: # for loop used to print each item in a list - each item is assigned to the variable magician
    print(magician)
print("\n") # line break between exercises - has nothing to do with exercise


#### Doing more work within a for loop
magicians1 = ["alice", "david", "carolina"] # new list
for magician in magicians1: # for loop used to print a string containing the value of the 'magician' variable on each iteration of the loop - uses f-string to add varible value to the string
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n") # added another string to be printed to show that a for loop can contain several lines - each line will be performed on the variable value before moving to the next iteration
print("\n") # line break between exercises - has nothing to do with exercise


#### Do something after a for loop 
magicians2 = ["alice", "david", "carolina"]
for magician in magicians2: # example of a for loop printing each value in the list - each value is assigned to the variable 'magician' on an iteration
    print(magician)
print("Thank you, everyone. That was a great magic show!") # print statement used to show that a line that isn't indented after a for loop will still be executed but not as part of the loop
print("\n") # line break between exercises - has nothing to do with exercise


#### avoiding indentation errors 
magicians3 = ["alice", "david", "carolina"] # new list
#for magician in magicians3: # ONLY COMMENTED OUT TO ALLOW THE REST OF THE PROGRAM TO WORK 
#print(magician) # this will cause an 'IndentationError' because the print statement isn't indented and not considered part of the for loop - only causes this error if no other indented line is in the for loop
print("\n") # line break between exercises - has nothing to do with exercise


#### Forgetting to Indent Additional Lines 
magicians4 = ["alice", "david", "carolina"] # new list
for magician in magicians4:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n") # This line should be indented so that it is executed on each iteration of the loop - it instead only runs once after the loop has finished and using the last value assigned to the varible 'magician' - doesn't cause an error though


#### Indenting Unnecessarily After the Loop
magicians5 = ["alice", "david", "carolina"] # new list
for magician in magicians5:
    print(f"{magician.title()}, that was a great trick!") # this should be indented so it's in the loop
    print(f"I can't wait to see your next trick, {magician.title()}.\n") # this should be indented so it's in the loop

    print("Thank you everyone, that was a great magic show!") # repeats everytime loop does because it's indented - this shouldn't be indented and only is to show how indentation can cause problems (logical error)


#### Forgetting the colon 
magicians6 = ["alice", "david", "carolina"] # new list
#for magician in magicians6     # 'SyntaxError' caused by not adding the colon - only commented out so the rest of the program can run
#    print(magician)


#### 