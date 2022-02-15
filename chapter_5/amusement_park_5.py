#### if-elif-else chain - Chapter 5
age = 12 
if age < 4:
    print("Your admission cost is £0.")
elif age < 18:
    print("Your admission cost is £25.")
else:
    print("Your admission cost is £40")

## A simpler way to do the above exercise - more efficient because you would only have to change string in one place instead of three like above
age = 12
if age < 4:
    price = 0
elif age < 18: # you can technically have as many 'elif' blocks as you want 
    price = 25
elif age < 65:
    price = 40
else:   # an 'else' block isn't always required and could be replaced by a 'elif' block to make it more specific - avoids random data or maulicious code causing an error 
    price = 20

print(f"Your admission cost is ${price}..")