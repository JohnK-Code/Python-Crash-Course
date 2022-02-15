#### TRY IT YOURSELF - Chapter 5 - Hello Admin
usernames = ["john", "kirsty", "sophie", "georgie", "admin", "eva"]
for user in usernames:
    if user == "admin":
        print(f"Hello {user.title()}, would you like a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")