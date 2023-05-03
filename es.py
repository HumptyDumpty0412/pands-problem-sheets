#Write a program that reads in a text file and outputs the number of e's it contains.
#The program should take the filename from an argument on the command line. 

#Author: Elena Chikanchi

import sys #I choose sys module because it works with my VS code
# I need sys.argv works with string (my textfile) and return argument [1] (my text)

with open(sys.argv[1], encoding='utf-8') as file: 
    #Use encoding = "utf-8" because my .txt doesnt read 
    
    text = file.read()
    
    n = text.count("e")
    # I need count all e letters in my text
    
    print(n)


