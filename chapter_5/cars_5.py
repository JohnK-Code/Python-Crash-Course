#### Cars - if statements 
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars: # loops through cars in list 'cars'
    if car == 'bmw': # if list value = 'bmw' change all letters to uppercase
        print(car.upper())
    else:
        print(car.title()) # if list value not equal to 'bmw' change first letter in string to uppercase


#### Checking for Equality
car = "bmw"
print(car == "bmw") # checks if the value of car is 'bmw' - This returns True

car = "audi"
print(car == 'bmw') # checks if the value of car is 'bmw' - This returns False

car = 'Audi'
print(car == 'audi') # checks if the value of car is 'audi' - This returns False because testing for Equality is case sensitive

car = 'Audi'
print(car.lower() == 'audi') # checks if the value of car is 'audi' - This returns True because we make the car variable value lowercase

car = 'Audi'
print(car.lower() == 'audi') # checks if the value of car is 'audi' - This returns True because we make the car variable value lowercase
print(car) # This shows that the 'lower()' method used on the car variable did not change it permenantly 
