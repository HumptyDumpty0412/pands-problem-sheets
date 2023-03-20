# This program ptints out random fruits
# Author: Elena Chikanchi

import random
fruits = ("Apple", "Orange", "Bannana", "Pear")
index = random.randint (0, len(fruits)-1)
fruit = fruits[index] 
print("A random fruit:{}" .format(fruit))
