#### TRY IT YOURSELF - Chapter 5 - Checking Username
current_users = ["david", "Bill", "ben", "noddy", "Eric"]
new_users = ["john", "Kirsty", "noddy", "stan","eric"]

current_users_lower = [user.lower() for user in current_users]

for users in new_users:
    if users.lower() in current_users_lower:
        print(f"The username {users} is not available, please try another!")
    else:
        print(f"The username {users} is available!")