#### TRY IT YOURSELF - More Loops

### this section is from a previous exercies - foods_4.py
# Copying a List
my_foods = ["pizza", "falafel", "carrot cake"]    # new list
friend_foods = my_foods[:]    # copy entire list using square brackets (slice) without index numbers for the start and end - If we don't use the square brackets (slice) then we wouldn't make a copy and both variables would just point to the same list

my_foods.append("cannoli")    # add item to list using 'append()' method to prove they are two seperate lists
friend_foods.append("ice cream")    # add item to list using 'append()' method to prove they are two seperate lists

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
### this section is from a previous exercies - foods_4.py

#### all code below is for this exercise and all code above is from a previous exercise - foods_4.py
print("My favorite foods using a for loop:")
for food in my_foods:
    print(food.title())

print("My friend's favorite food using a for loop")
for food in friend_foods:
    print(food.title())