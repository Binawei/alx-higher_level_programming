#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#To Get the string representation
num =repr(number)
#Accessing the last string
digit = num[-1]
#converting back to an integer
digit = int(digit)
if digit > 5:
   print("Last digit of {} is {} and is greater than 5".format(number, digit))
elif (digit < 6) & (digit != 0):
   print("Last digit of {} is {} and is less than 6 and not 0".format(number, digit))
else:
    print("Last digit of {} is {} and is 0.".format(number, digit))

