
import math
import os
import random
import re
import sys


print("\n **** Sales by Match  **** \n")

print("There is a large pile of socks that must be paired by color. Given")
print("an array of integers representing the color of each sock, determine")
print("how many pairs of socks with matching colors there are. \n")

print("Example:")
print("n = 7")
print("ar = [1, 2, 1, 2, 1, 3, 2] \n")

print("There is one pair of color 1 and one of color 2. There are three odd")
print("socks left, one of each color. The number of pairs is 2. \n")



ar = [1, 2, 1, 2, 1, 3, 2]
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]


Pairs_Dict = {}
Pairs_Complete = 0

for sock in ar:

    if sock in Pairs_Dict.keys():

        Pairs_Dict[sock] = Pairs_Dict[sock] + 1

    else:
        
        Pairs_Dict[sock] = 1


for color in Pairs_Dict:

    Socks = Pairs_Dict[color]
    Pair = Socks//2

    Pairs_Complete = Pairs_Complete+Pair


print(Pairs_Complete)





    

    
