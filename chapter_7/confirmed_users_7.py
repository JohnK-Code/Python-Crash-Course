#### Chapter 7 - Confirmed Users - Moving Items from One List to Another
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list if confirmed users.
while unconfirmed_users: # runs while list not empty - empty list is equal False 
    current_user = unconfirmed_users.pop() # remove and save the last item in 'unconfirmed_users' to the variable 'current_user'
    print(f"Verify user: {current_user.title()}")
    confirmed_users.append(current_user) # add 'current_user' to 'confirmed_users' list
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users: # loop through 'confirmed_users' and print each 
    print(confirmed_user.title())