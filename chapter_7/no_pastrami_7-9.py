#### TRY IT YOURSELF - Chapter 7 - No Pastrami
sandwich_orders = ['cheese and ham', 'pastrami', 'philly cheesesteak', 'tuna mayo', 'pastrami', 'coronation chicken', 'pastrami'] # list of sandwich orders
finished_sandwiches = [] # empty list of finished sandwiches

print("We have run out of Pastrami sorry.") # notify user that there is no 'pastrami'
while 'pastrami' in sandwich_orders: # 'while' 'pastrami' in list run below indented code  
    sandwich_orders.remove('pastrami') # remove the first instance of the 'pastrami' value from the lis using 'remove()' method

while sandwich_orders: # run 'while' loop until 'sandwich_orders' list is empty
    current_sandwich = sandwich_orders.pop() # 'pop()' (remove) the last item in the list and add it to the 'current_sandwich' variable 
    print(f"I'm currently making your {current_sandwich.title()} sandwich.") # print message about the 'current_sandwich'
    finished_sandwiches.append(current_sandwich) # add value from 'current_sandwich' to the end of the 'finished_sandwiches' list 

print("The following sandwich orders have been completed:") # print this message when 'while' loop is finished
for sandwich in finished_sandwiches: # for every 'value' in the 'finished_sandwiches' list run below indented code
    print(f"\t{sandwich.title()}") # print the value of the 'sandwich' variable and make the first letter of every word uppercase using the 'title()' method