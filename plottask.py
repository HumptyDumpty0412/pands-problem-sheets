# This program displays:

#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
 
#and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

#Author: Elena Chikanchi

import numpy as np

import matplotlib.pyplot as plt

# Create numeric sequences 
x = np.linspace(0,10,1000)
y1 = [i**3 for i in x]
y2 = np.random.normal(0,2,1000)

#Creat coordinate axes

plt.title("Title Grafics",fontsize=17)
plt.xlabel("Text X")
plt.ylabel("Text Y")
plt.grid()

plt.plot(x, y1, label="Grafic x**3")
plt.hist(y2, label="Gistogramm")


plt.legend()
plt.show()



