
# Lonely Integer

print("\n ****  Lonely Integer  **** \n")

print("Given an array of integers, where all elements but one occur twice,")
print("find the unique element. \n")

print("Example:")
print("a = [1, 2, 3, 4, 3, 2, 1] \n")

print("The unique element is: 4 \n")


# Solution --------------------------------------------------------------

import math
import os
import random
import re
import sys


a = [1, 2, 3, 4, 3, 3, 2, 1]


print(f" Array to check: {a}")

for item in a:

    Count = a.count(item)

    if(Count == 1):

        break


print(f" Unique item = {item}")

    
