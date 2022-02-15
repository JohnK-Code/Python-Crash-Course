#### Numerical Inequality 
answer = 17 
if answer != 42: # Check if 'answer' is not equal to '42'
    print("That is not the correct answer. Please try again!") #  This code will run because the value of 'answer' is not equal to 42


#### Other Mathmatical Comparisons
age = 19
print(age < 21) # checks if the value of the 'age' variable is less than 21 - True

print(age <= 21) # checks if the value of the variable 'age' is equal to or less than 21 - True

print(age > 21) # checks if the value of the variable 'age' is more than 21 - False

print(age >= 21) # checks if the value of the variable 'age' is equal to or more than 21


#### Using 'and' to check multipe conditions 
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # check if the values of both 'age_0' and 'age_1' are equal to or greater than 21 - False because only one value is equal or greater than 21

age_1 = 22 # change the value of 'age_1' to 22 
print(age_0 >= 21 and age_1 >= 21) # check if the values of both 'age_0' and 'age_1' are equal to or greater than 21 - True becuase both variable values are equal or greater than 22 unlike last time when only one value was
print((age_0 >= 21) and (age_1 >= 21)) # Same as above example but uses parentheses around each test - Parentheses make no difference they just make the code look cleaner


#### Using 'or' to Check Multiple Conditions
age_00 = 22
age_01 = 18 
print(age_00 >= 21 or age_01 >= 21) # Uses 'or' - Returns 'True' if either of the conditions are correct unlike 'and' above that needs both to be correct to return 'True' - Both would need to be incorrect using 'or' to return 'False'

age_00 = 18
print(age_00 >= 21 or age_01 >= 21) # Returns 'False' when using 'or' because both conditions are incorrect


#### Check Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # Uses 'in' to check if a specified value is in a list - Returns 'True' because 'mushrooms' is in the list
print('pepperoni' in requested_toppings) # Returns 'False' because 'pepperoni' is not in the list