#### Chapter 9 - Creating and Using a Class - Creating the Dog Class

class Dog:  # 'Define' a 'Class' called 'Dog'
    """A simple attempt to model a dog.""" # 'docstring'
    
    # 'define' a function - A 'function' is also called a 'method' when it is part of a 'class'
    # '__init__' methods are automatically run when a new 'instance' is created based on the 'Dog' 'Class'
    # The 'self' paramater is required and must come first in the '__init__' method - 
    # 'self' gives the 'instances' created using the 'class' access to the 'attributes' and 'methods' in the class 
    def __init__(self, name, age): 
        """Initialize name and age attributes.""" # 'docstring'
        self.name = name # These types of variables are called 'attributes'
        self.age = age # These types of variables are called 'attributes'

    def sit(self): # defining a 'method' - This will be available to any 'instance/object' created using this 'Class'
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self): # defining a 'method' - This will be available to any 'instance/object' created using this 'Class'
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


#### Making an 'instance' from a 'Class'
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")


#### Accessing Attributes
my_dog.name # To acces the 'attribute' of an 'instance' created from a 'Class', you use dot notation - The 'objects/instance' name is followed by the 'attribute' name seperated by a dot - This is the same 'self.name' attribute from the 'class'
my_dog.age # To acces the 'attribute' of an 'instance' created from a 'Class', you use dot notation - The 'objects/instance' name is followed by the 'attribute' name seperated by a dot - This is the same 'self.name' attribute from the 'class'


#### Calling Methods 
my_dog.sit() # To access the 'method' of an 'instance/object' created from a 'Class, you use dot notation - This is the same method that was defined in the 'Dog' 'Class' but is now being accessed though the 'instance' created from it
my_dog.roll_over() # To access the 'method' of an 'instance/object' created from a 'Class, you use dot notation - This is the same method that was defined in the 'Dog' 'Class' but is now being accessed though the 'instance' created from it


#### Creating Multiple Instances
my_dog1 = Dog('Willie', 7) # making an 'instance/object' from a 'Class' - You can make as many as you wan't from a 'Class'
your_dog = Dog('Lucy', 3) # making an 'instance/object' from a 'Class' - You can make as many as you wan't from a 'Class'
print(f"\nMy dog's name is {my_dog1.name}.") # accessing 'attribute' from an 'object/instance'
print(f"My dog is {my_dog1.age} years old.") # accessing 'attribute' from an 'object/instance'
my_dog1.sit() # accesing a 'method' from an 'object/instance'
print(f"\nYour dog's name is {your_dog.name}.") # accessing 'attribute' from an 'object/instance'
print(f"Your dog is {your_dog.age} years old.") # accessing 'attribute' from an 'object/instance'
your_dog.sit() # accesing a 'method' from an 'object/instance'