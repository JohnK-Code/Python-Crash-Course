#### TRY IT YOURSELF - More Conditional Tests - Chapter 5

### String Comparisons

## Equality
car = 'honda'
print("Is car == 'honda'? I predict True.")
print(car == 'honda') # True

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi') # False

## Inequality
car1 = 'BMW'
if car1 != 'volkswagen': # True
    print("\ncar1 is not equal to your favorite car manufacturer 'volkswagen'.")

car1 = 'volkswagen'
if car1 != 'volkswagen': # False
    print("\ncar1 is not equal to your favorite car manufacturer 'volkswagen'.")
else:
    print("\ncar1 is equal to 'volkswagen' - This statement run because the if condition was False.")

## Using 'lower()' method
print("\n") # Line break
car2 = 'Ferrari'
print(car2.lower() == 'ferrari') # True
print(car2.lower() == 'lamborgini') # False


### Numerical Comparisons

##Equality
john = 32
print(john == 32) # True
print(john == 30) # False

##Inequality
kirsty = 28 
if kirsty != 30: # True
    print("\nThat is not the correct age for Kirsty.")
kirsty = 30
if kirsty != 30: # False
    print("\nThat is not the correct age for Kirsty.")
else:
    print("\nFalse")

##Greater than
print("\n") # Line Break
age = 30 
print(age > 25) # True
age = 25
print(age > 25) # False

##Less than
print("\n") # Line Break
age1 = 25
print(age1 < 30) # True
age1 = 30
print(age1 < 25) # False

##Greater than or equal to
print("\n") # Line Break
k_age = 30
print(k_age >= 30) # True 
k_age = 25 
print(k_age >= 30) # False

##Less than or equal to 
print("\n") # Line Break
j_age = 32
print(j_age <= 32) # True
print(j_age <= 30) # False

##Tests using the keyword 'and'
print("\n") # Line Break
age_50 = 50
age_40 = 40
print(age_40 >= 30 and age_50 >= 40) # True
print(age_40 <= 30 and age_50 <= 40) # False

##Tests using the keyword 'or'
print("\n") # Line Break
age_10 = 10
age_20 = 20 
print(age_10 >= 10 or age_20 <= 10) # True
print(age_10 >= 20 or age_20 <= 10) # False

##Test whether an item is 'in' a list 
print("\n") # Line Break
my_cars = ["civic", "106", "corsa", "coupe"]
print("civic" in my_cars) # True 
print("206" in my_cars) # False

##Test whether an item is 'not' in a list
print("\n") # Line Break 
print("206" not in my_cars) # True
print("106" not in my_cars) # False