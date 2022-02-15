# Copying a List
my_foods = ["pizza", "falafel", "carrot cake"]    # new list
friend_foods = my_foods[:]    # copy entire list using square brackets (slice) without index numbers for the start and end - If we don't use the square brackets (slice) then we wouldn't make a copy and both variables would just point to the same list

my_foods.append("cannoli")    # add item to list using 'append()' method to prove they are two seperate lists
friend_foods.append("ice cream")    # add item to list using 'append()' method to prove they are two seperate lists

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

