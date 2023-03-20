# The program reads in a student’s percentage mark and
# prints out corresponding the grade (the program should check that the
# percentage is valid

# Author: Elena Chikanchi

percentage = float(input("Enter the percentage:")) # print("persentage")
percentage = round(percentage) 
if percentage < 0 or percentage > 100:
    print( "Please enter a number between 0 and 100")
elif percentage < 40: # we know its greater than 0
    print("Fail")
elif percentage < 50: # between 40 and 49
    print("Pass")
elif percentage < 60: # between 50 and 59
    print("Merit2")
elif percentage < 70: # between 60 and 69
    print("Merit")
else: # The only option left between 70 and 100
    print("Distinction")
