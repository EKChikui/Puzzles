
# Sparse Arrays

import math
import os
import random
import re
import sys


print("\n ****  Sparse Arrays  **** \n")

print("There is a collection of input strings and a collection of query")
print("strings. For each query string, determine how many times it occurs")
print("in the list of input strings. Return an array of the results. \n")

print("Example:")
print("strings = ['ab', 'ab', 'abc']")
print("queries = ['ab', 'abc', 'bc'] \n")

print("There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each")
print("query, add an element to the return array, results = [2, 1, 0] \n")



# Solution --------------------------------------------------------------

strings = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]

print(f" Strings = {strings}")
print(f" Queries = {queries}")

Queries_Count = []

for item in queries:

    Counting = strings.count(item)
    Queries_Count = Queries_Count + [Counting]


print(f" Solution = {Queries_Count}")
