# This program should takes a positive floating-point number as input
# and outputs an approximation of its square root.
#  Not to use the built in functions x ** .5 or math.sqrt(x).
# Use Newton method 

# Author: Elena Chikanchi


# The Newton method is f(x)=0 
x = float(input("Please enter a positive number: ")) #Ask any float positive amount
guess = x / 2 #Guess doesnt know 
while guess * guess - x > 10e-12: #10e-12 its limit
    guess = (guess + x / guess) / 2
print("The square root is: ")
print(guess)
