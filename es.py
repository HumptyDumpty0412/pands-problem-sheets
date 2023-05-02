#Write a program that reads in a text file and outputs the number of e's it contains.
#The program should take the filename from an argument on the command line. 

#Author: Elena Chikanchi

import sys #

with open(sys.argv[1], encoding='utf-8') as file:
    text = file.read()
    n = text.count("e")
    print(n)


