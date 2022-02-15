#### Working with Classes and Instances 
## The Car Class

"""A set of classes used to represent gas and electric cars."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # setting an 'initial value' for an 'attribute'

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage): # modifying an 'attributes' value through a 'method'
        """
        Set odometer reading to the given value.
        Reject the change if it atempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, miles): # Incrementing an 'attribute' value thorugh a 'method'
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


class ElectricCar(Car): # define a 'Class' called 'ElectricCar' - In this example the 'Class' is a 'child' 'Class' of the 'Car' 'Class' - 'Inherits' from 'Car' 'class'
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year): # define a 'method'
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) # the 'super()' 'function' is a special function that allows you to call a 'method' from a 'parent' 'class' - The name 'super' comes form the convention of calling the 'parent' class a 'superclass' and a 'child' class a 'subclass'
        self.battery = Battery() # 'Instance/Object' as an 'Attribute'



# Commented out so class can be imported into another file  without the below code running
""" 
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23 # Modifying an 'Attribute's' Value Directly using dot notation
my_new_car.read_odometer() # accessing a 'method' using dot notation - checking 'odometer_reading' 'attribute' has been updated

my_new_car.update_odometer(20) # accessing a 'method' using 'dot notation' - updating an 'attribute' value using a 'method'
my_new_car.read_odometer() # accessing a method using dot notation - checking the 'odometer_reading' 'attribute' has been updated  
print("\n") # Just a line break 


my_used_car = Car('subaru', 'outback', 2015) # creating a NEW 'instance' of the 'Class' 'Car'
print(my_used_car.get_descriptive_name()) # accessing a 'method' using dot notation
my_used_car.update_odometer(23_500) # accessing a 'method' using dot notation - updating the 'value' of the 'odometer_reading' 'attribute' using the 'update_odometer' 'method'
my_used_car.read_odometer() # accessing a 'method' using dot notation - checking the 'odometer_reading' 'attribute' has been updated
my_used_car.increment_odometer(100) # accessing a 'method using dot notation - 'Adding' the specified 'value' to the 'value' already in the 'attribute' 'odomter_reading'
my_used_car.read_odometer() # accesing a 'method' using dot notation - checking the 'value' has been added to the 'value' in the 'odometer_reading' 'attribute' using the 'increment_odometer' 'method' on the above line
"""