# The program write  that the user asks to input any positive integer and outputs the successive 
# values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, 
# divide it by two, but if it is odd, multiply it by three and add one.

# Have the program end if the current value is one.
# Author : Elena Chikanchi

# Suracusa sequence:choose any digit. Even or Odd:odd numbers count like "x:2"
# Even numbers count like "3x+1"


x = int(input("Please enter any digit x:\n")) # need transform in input because its digit
 
while x > 1:     #Final point is 1, so while till x = 1   =>    x>1
  print (x, end =" ") # I pun end = " " in both prints in order to see results like string, not colomn
  if x % 2 == 0:  # if and else should be equal in line
   x = x // 2
  else:
   x = 3*x+1
print(x, end="")



