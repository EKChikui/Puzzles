
import math
import os
import random
import re
import sys


print("\n ****  Pangram  **** \n")

print("A pangram is a string that contains every letter of the alphabet.")
print("Given a sentence determine whether it is a pangram in the English")
print("alphabet. Ignore case. Return either pangram or not pangram as")
print("appropriate. \n")

print("Example:")
print("s = The quick brown fox jumps over the lazy dog \n")
print("The string contains all letters in the English alphabet, so return")
print("pangram. \n")


# Solution --------------------------------------------------------------

String = "The quick brown fox jumps over the lazy dog"
#String = "We promptly judged antique ivory buckles for the next prize"
#String = "We promptly judged antique ivory buckles for the prize"

Pangram = {"a": 0, "b": 0, "c": 0 ,"d": 0, "e": 0, "f": 0,
           "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
           "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
           "s": 0, "t": 0, "u": 0, "v": 0, "x": 0, "y": 0,
           "w": 0, "z": 0, " ": 0 }


String_Letters = list(String)

for letter in String_Letters:

    letter = letter.lower()
    Pangram[letter] = Pangram[letter]+1


Missing_Letters = []

for letter in Pangram:

    if(Pangram[letter] == 0):

        Missing_Letters = Missing_Letters + [letter]


if(len(Missing_Letters) == 0):

    print("Answer = pangram")

else:

    print("Answer = Not pangram")
    print(Missing_Letters)

