
# Plus Minus

print("\n ****  Plus Minus  **** \n")

print("Given an array of integers, calculate the ratios of its elements")
print("that are positive, negative, and zero. Print the decimal value of")
print("each fraction on a new line with  places after the decimal. \n")

print("Note: This challenge introduces precision problems. The test cases")
print("      are scaled to six decimal places, though answers with absolute")
print("      error of up to are acceptable. \n")


# Solution --------------------------------------------------------------

import math
import os
import random
import re
import sys


#arr = [-4, 3, -9, 0, 4, 1]
arr = [1, 2, 3, -1, -2, -3, 0, 0]
  
Negatives = 0
Zeros = 0
Positives = 0
Total = 0    

for item in arr:
    
    if(item < 0):
        Negatives = Negatives+1
    
    if(item > 0):
        Positives = Positives+1
    
    if(item == 0):
        Zeros = Zeros+1
    
    Total = Total+1


Freq_Negative = round(Negatives/Total, 6)
Freq_Zero = round(Zeros/Total, 6)
Freq_Positive = round(Positives/Total, 6)


print(Freq_Positive)
print(Freq_Negative)
print(Freq_Zero)


# Closing

print("\n * \n")    
        
    
    

