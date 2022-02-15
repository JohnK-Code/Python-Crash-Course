#### TRY IT YOURSELF - Chapter 9 - Page 181 - Dice
from random import randint, randrange
class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

# six sided dice
d6 = Die()
results = []
for roll_num in range(10):
    roll = d6.roll_die()
    results.append(roll)
print(results)

# ten sided dice 
d10 = Die(sides=10)
results = []
for roll_num in range(10):
    roll = d10.roll_die()
    results.append(roll)
print(results)

# twenty sided die
results = []
d20 = Die(sides=20)
for roll_num in range(10):
    roll = d20.roll_die()
    results.append(roll)
print(results)