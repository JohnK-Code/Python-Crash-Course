#### TRY IT YOURSELF - Chapter 9 - Multiple Modules - User Class
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