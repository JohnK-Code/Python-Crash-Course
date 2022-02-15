#### TRY IT YOURSELF - Chapter 9 - Page 174 - Battery Upgrade
## code from previous exercise 'electric_car_9.py - Modified 

class Car: # define the 'Car' 'Class' - Used as a 'parent' 'Class' in this example
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year): # define the '__init__' method
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # setting an 'initial value' for an 'attribute'

    def get_descriptive_name(self): # define a method
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self): # define a method
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): # define a method - modifying an 'attributes' value through a 'method'
        """
        Set odometer reading to the given value.
        Reject the change if it atempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles): # define a method - Incrementing an 'attribute' value thorugh a 'method'
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery: # define a 'class' called 'Battery' that doesn't inherent from any other 'class'
    """A Simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battry's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"The battery has been upgraded to {self.battery_size}-kWh.")
        else:
            print("The battery is already upgraded.")

class ElectricCar(Car): # define a 'Class' called 'ElectricCar' - In this example the 'Class' is a 'child' 'Class' of the 'Car' 'Class'
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # define a 'method'
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) # the 'super()' 'function' is a special function that allows you to call a 'method' from a 'parent' 'class' - The name 'super' comes form the convention of calling the 'parent' class a 'superclass' and a 'child' class a 'subclass'
        self.battery = Battery() # 'Instance/Object' as an 'Attribute'

tesla = ElectricCar('tesla', 'model s', 2020)
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()
tesla.battery.upgrade_battery()