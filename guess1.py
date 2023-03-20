# This a program that prompts the user to guess a number
# Program should keep prompting the user to guess the number until the user
# gets the right on

# Author: Elena Chikanchi

numberToGuess = 30

guess = int(input("Please guess a number:"))
while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again:")) # symmetry is important 

print ("Well done! Yes a number was ",numberToGuess)