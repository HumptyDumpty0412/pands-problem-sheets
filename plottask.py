# This program displays:

#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
 
#and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

#Author: Elena Chikanchi

import numpy as np

import matplotlib.pyplot as plt

fig = plt.figure (figsize=(5,1000))
# I use fig/figsize to create a boards of plot. 
ax = fig.add_subplot()

y=np.random.normal (0,2,1000)
ax.hist(y)
ax.grid()

plt.legend()
plt.show()

#def f(x):
    #x=np.array(x)
    #return 1.0/x*3
#print(f(3))