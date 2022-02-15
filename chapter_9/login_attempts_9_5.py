#### TRY IT YOURSELF - Chapter 9 - Login Attempts - Page 167
## Copy of exercise users_9_3.py to be modified
class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, age, email, city):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.email = email
        self.city = city
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increment the value of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login attempts to 0."""
        self.login_attempts = 0

user = User('john', 'kelly', 32, 'test@email.com', 'glenrothes')
print(f"Login Attempts: {user.login_attempts}")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login Attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login Attempts: {user.login_attempts}")