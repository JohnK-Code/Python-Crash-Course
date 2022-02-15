#### TRY IT YOURSELF - Chapter 9 - Page 180 - Multiple Modules - Privileges & Admin Classes
from multiple_modules_user_9_12 import User
class Admin(User):
    """Represent an admin user."""

    def __init__(self, first_name, last_name, age, email, city):
        """
        Initialize attributes of the parent class.
        Then initialize attributes to to describe an admin user.
        """
        super().__init__(first_name, last_name, age, email, city)
        self.privileges = Privileges()


class Privileges:
    """Represent a users privileges."""
    
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the privileges an admin user has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")