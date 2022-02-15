#### TRY IT YOURSELF - Chapter 9 - Ice Cream Stand - Page 173
## Code form previous exercise 'restaurant_9_1.py'
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Return a neatly formatted description of a restaurant."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"The restaurant serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Return a message stating the restaurant is open."""
        print(f"{self.restaurant_name} is open.")

## New Code
class IceCreamStand(Restaurant):
    """A simple attempt to model a Ice Cream Stand."""

    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        """
        Initialize attributes of the parent class.
        Then initialize attributes to to describe a Ice Cream Stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'chocolate', 'mint choc chip', 'caramel']

    def show_flavors(self):
        print("Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("visochi's")
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
ice_cream_stand.open_restaurant()