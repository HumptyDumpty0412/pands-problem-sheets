# The program outputs whether or not today is a weekday or weekend
# Author : Elena Chikanchi

x = input(" What is a day today? :") # I need to create 2 lists: weekday & weekend
weekday = ["Monday","Thuesday","Wednesday","Thursday","Friday"]
weekend = ["Saturday","Sunday"]
while True:
    if x in weekday:
        print("Unfortunately,today is weekday")
        break # need break to stop clonning strings in both cases
    else: 
        if x in weekend:
            print("Today is weekend,yay!")
            break
