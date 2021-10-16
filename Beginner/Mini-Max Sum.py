
# Mini-Max Sum

print("\n ****  Mini-Max Sum  **** \n")

print("Given five positive integers, find the minimum and maximum values")
print("that can be calculated by summing exactly four of the five integers.")
print("Then print the respective minimum and maximum values as a single")
print("line of two space-separated long integers. \n")

print("Example:")
print("arr = [1, 3, 5, 7, 9]")
print("The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3+5+7+9 = 24.")
print("The function prints: 16 24 \n")


# Solution --------------------------------------------------------------



# Closing

import math
import os
import random
import re
import sys


arr = [1, 2, 3, 4, 5]
arr = [7, 69, 2, 221, 8974]

    
Min_Sum = 999999999999999
Max_Sum = 0

i = 0
while(i < len(arr)):
    
    arr_copy = arr[:]
    arr_copy.pop(i)
    Sum = sum(arr_copy)
    
    if(Sum < Min_Sum):
        Min_Sum = Sum
    
    if(Sum > Max_Sum):
        Max_Sum = Sum
    
        
    i = i+1

print(Min_Sum, Max_Sum)


# Closing

print("\n * \n")


        
