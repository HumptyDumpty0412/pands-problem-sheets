# Write a python program
# that reads in a 10 character account number
# and outputs the account number with only the last 4 digits showing
# (and the first 6 digits replaced with Xs).

# Author: Elena Chikanchi (Im write a recipe)

a = int(input("Please enter an 10 digit account number: ")) #int(input) despite the 10
x = "0123456789" # I need to show last 4 digits so 1)"replace"function  it doesnt work
                 # "len(x)" doesnt work. Put "0"in beginning (start counting). Using "list"
print("XXXXXX"+x[6:]) 