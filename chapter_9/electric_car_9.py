#### Inheritance - Electric Car - Chapter 9 - Page 167-168
## The __init__() Method for a Child Class
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

class ElectricCar(Car): # define a 'Class' called 'ElectricCar' - In this example the 'Class' is a 'child' 'Class' of the 'Car' 'Class'
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # define a 'method'
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) # the 'super()' 'function' is a special function that allows you to call a 'method' from a 'parent' 'class' - The name 'super' comes form the convention of calling the 'parent' class a 'superclass' and a 'child' class a 'subclass'
        #self.battery_size = 75 # define an 'attribute' that is specific to the 'ElectricCar' class and not the 'inhereted' 'Car' 'Class' - This has an 'initial value' of 75
        self.battery = Battery() # 'Instance/Object' as an 'Attribute'

    #def describe_battery(self): # define a 'method' - This 'method' is specific to the 'ElectricCar' 'class' and not 'inherited' from the 'parent' 'class'
    #    """Print a statement describing the battery size."""
    #    print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019) # create an instance of the 'class' 'ElectricCar'
print(my_tesla.get_descriptive_name()) # access a method of the 'instance/object' 'my_tesla'
#my_tesla.describe_battery() # access a method of the 'instance/object' 'my_tesla'
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()