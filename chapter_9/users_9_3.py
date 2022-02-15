#### TRY IT YOURSELF - Chapter 9 - Users
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

user1 = User('john', 'kelly', 32, 'test@email.com', 'Glenrothes')
user1.describe_user()
user1.greet_user()

user2 = User('kirsty', 'murray', 30, 'test1@email.com', 'Glenrothes')
user2.describe_user()
user2.greet_user()

user3 = User('david', 'mugg', 67, 'test2@email.com', 'padanaram')
user3.describe_user()
user3.greet_user()