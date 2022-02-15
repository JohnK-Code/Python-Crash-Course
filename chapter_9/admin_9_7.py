#### TRY IT YOURSELF - Chapter 9 - Page 173 - Admin
## Code from previous exercise 'users_9_3.py'
class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, age, email, city):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.email = email
        self.city = city

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"City: {self.city.title()}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}.\n")

## New code 
class Admin(User):
    """Represent an admin user."""

    def __init__(self, first_name, last_name, age, email, city):
        """
        Initialize attributes of the parent class.
        Then initialize attributes to to describe an admin user.
        """
        super().__init__(first_name, last_name, age, email, city)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the privileges an admin user has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin('john', 'kelly', '32', 'test@test.com', 'glenrothes')
admin.describe_user()
admin.show_privileges()