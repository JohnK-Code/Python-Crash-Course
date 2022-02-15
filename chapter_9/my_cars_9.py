#### Importing Multiple Classes - Chapter 9 - Page 177
from car_9 import Car, ElectricCar # 'Importing' 'Car' and 'ElectricCar' 'Class' from 'car_9.py' - 2019 cars
import car_9 # 'importing' entire 'Module' - Uses the dot notation shown in last two created instances - 2020 cars
#from module_name import *       ## Importing all classes from a module

my_bettle = Car('volkswagen', 'bettle', 2019) # create instance of a class using specific class name
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019) # create instance of a class using specific class name
print(my_tesla.get_descriptive_name())

my_bettle1 = car_9.Car('volkswagen', 'bettle', 2020) # create 'instance' of a 'class' using 'file/module' name and 'class' name using 'dot notation' 
print(my_bettle1.get_descriptive_name())

my_tesla1 = car_9.ElectricCar('tesla', 'roadster', 2020) # create 'instance' of a 'class' using 'file/module' name and 'class' name using 'dot notation' 
print(my_tesla1.get_descriptive_name())