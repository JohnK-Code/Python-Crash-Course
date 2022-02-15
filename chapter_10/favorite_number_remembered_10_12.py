#### TRY IT YOURSELF - Chapter 10 - Page 208 - Favorite Number Remembered 
import json

def favorite_num():
    """Report favorite number if it exists, or create it then report it."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
           favorite_num =  json.load(f)
    except FileNotFoundError:
        favorite_num = input("What is your favorite number? ")
        with open(filename, 'w') as f:
            json.dump(favorite_num, f)
            print(f"Your favorite number is {favorite_num}, I will save it for later.")
    else:
        print(f"Your favorite number is {favorite_num}.")

favorite_num()