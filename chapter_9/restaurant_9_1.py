#### TRY IT YOURSELF - Chapter 9 - Restaurant
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Return a neatly formatted description of a restaurant."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"\nThe restaurant serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Return a message stating the restaurant is open."""
        print(f"\n{self.restaurant_name} is open.")

foxtons = Restaurant('foxtons', 'mexican')
print(foxtons.restaurant_name)
print(foxtons.cuisine_type)
foxtons.describe_restaurant()
foxtons.open_restaurant()