# This program should:
# Prompt the user and read in two money amounts (in cent)
# Add the two amounts
# Print out the answer in a human readable format with a euro sign 
# and decimal point between the euro and cent of the amount

# Author: Elena Chikanchi 

a=int(input("Please enter the first number in cent: "))
b=int(input("Please enter the second number in cent: "))
string=((a+b)/100)

print(f" The sum of number of these is {string} euro")
      
