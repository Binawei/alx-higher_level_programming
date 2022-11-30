#!/usr/bin/python3
j = 0
for i in range(0, 98):
   while j < 98:
          if i < j or i != j:
               #if (i != 8) or (i == 8 & j != 9):
               print("{:02}".format(j), end=", ")
          j += 1
print("{}".format(89))
