#### TRY IT YOURSELF - Chapter 10 - Page 208 - Favorite Number 
import json

def request_favorite_num():
    """Request the users favorite number and save it to a file."""
    number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)

def check_favorite_num():
    """Get file and display favorite number in message."""
    filname = 'favorite_number.json'
    try:
        with open(filname) as f:
            fav_num = json.load(f)
            print(f"I know your favorite number! it's {fav_num}.")
    except FileNotFoundError:
        print("The specified file cannot be found.")

request_favorite_num()
check_favorite_num()