
print("What is a day today?:")
weekday = ("Monday","Thuesday","Wednesday","Thursday","Friday")
while weekday:
    guess = input("weekday:")
    if guess in weekday:
        print("Yes,unfortunatly today is weekday", guess)
    else:
        print("It is the weekend,ya!") 