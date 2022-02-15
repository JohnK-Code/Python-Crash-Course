#### TRY IT YOURSELF - Chapter 9 - Three Restaurants
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Return a neatly formatted description of a restaurant."""
        print(f"\nThe restaurant is called {self.restaurant_name}.")
        print(f"The restaurant serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Return a message stating the restaurant is open."""
        print(f"\n{self.restaurant_name} is open.")

restaurant1 = Restaurant('foxtons', 'mexican')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('frankie & bennies', 'italian')
restaurant2.describe_restaurant()

restaurant3 = Restaurant("tony's", 'american')
restaurant3.describe_restaurant()