#### TRY IT YOURSELF - Chapter 10 - Page 208 - Verify User 
import json

def get_stored_username(): 
    """Get stored username iis available.""" 
    filename = 'username.json' 
    try: 
        with open(filename) as f: 
            username = json.load(f) 
    except FileNotFoundError: 
        return None 
    else:
        print(f"Is {username} your username?")
        check_user = input("If yes enter 'y', if no enter 'n': ")
        if check_user == 'y':
            return username 
        else: 
            return None


def get_new_username(): 
    """Prompt for a new username.""" 
    username = input("What is your name? ") 
    filename = 'username.json' 
    with open(filename, 'w') as f: 
        json.dump(username, f) 
    return username


def greet_user(): 
    """Greet the user by name."""
    username = get_stored_username() 
    if username: 
        print(f"Welcome back, {username.title()}!") 
    else: 
            username = get_new_username() 
            print(f"We'll remember you when you come back, {username.title()}!") 


greet_user()