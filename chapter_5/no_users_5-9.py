#### TRY IT YOURSELF - Chapter 5 - No Users
usernames = []
if usernames:   # Checks if 'usernames' list is empty - runs indented code if list not empty
    for user in usernames: # loops through 'usernames' list
        if user == "admin": # runs indented code if list value equals 'admin'
            print(f"Hello {user.title()}, would you like a status report?")
        else:   # runs if list value not equal to 'admin'
            print(f"Hello {user.title()}, thank you for logging in again.")
else:   # runs indented code if 'usernames' list is empty
    print("We need to find some users!")