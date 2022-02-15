#### TRY IT YOURSELF - Chapter 9 - Number Served - Page 167
## Copy of program from exercise restaurant_9_1.py to be updated
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Return a neatly formatted description of a restaurant."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"\nThe restaurant serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Return a message stating the restaurant is open."""
        print(f"\n{self.restaurant_name} is open.")

    def set_number_served(self, num_customers):
        """Set the number of customers that have been served."""
        self.number_served = num_customers

    def increment_number_served(self, customers):
        """Increment the number of customers that have been served."""
        self.number_served += customers

restaurant = Restaurant('jimmy chungs', 'chinese')
print(restaurant.number_served)
restaurant.number_served = 25
print(restaurant.number_served)
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)