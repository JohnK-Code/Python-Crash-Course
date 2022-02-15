#### TRY IT YOURSELF - Chapter 8 - Imports 
## Using different import methods and function call methods 

import imports_8_16 
imports_8_16.make_pizza(12, 'cheese', 'ham')


from imports_8_16 import make_pizza
make_pizza(6, 'pineapple', 'extra cheese')


from imports_8_16 import make_pizza as mp
mp(12, 'pepperoni', 'spicy cheese')


import imports_8_16 as im
im.make_pizza(12, 'chocolate', 'cheese')


from imports_8_16 import * 
make_pizza(10, 'peach', 'test')