#That program print out random fruits
#Author: Elena Chikanchi

import random
fruits = ["Apple","Orange","Pear","Bannana"]
# We want a random number between 0 and lenght-1
index = random.randint (0,len(fruits)-1)
fruit = fruits [index]
print ("A Random fruit:{}". format(fruit))
      
