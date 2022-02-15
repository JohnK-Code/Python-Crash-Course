#### TRY IT YOURSELF - Buffet
buffet_foods = ("chips", "chicken curry", "rice", "pizza", "salt & pepper chicken balls") # new tuple 
print("This is some of the items available at the buffet:")
for food in buffet_foods:
    print(food.title())

# buffet_foods[1] = "pakora" - Commented out to allow rest of program to work - TypeError: 'tuple' object does not support item assignment - Can't change items in a tutple 

print("\n") # new line

print("The buffet has changed some of the items on the Menu")
print("Below is the new menu:")
buffet_foods = ("potatoes", "tikka masala", "rice", "pizza", "salt & pepper chicken balls")
print(buffet_foods)