
import math
import os
import random
import re
import sys


print("\n ****  Julius Caesar Cipher  **** \n")

print("Julius Caesar protected his confidential information by encrypting")
print("it using a cipher. Caesar's cipher shifts each letter by a number of")
print("letters. If the shift takes you past the end of the alphabet, just")
print("rotate back to the front of the alphabet. In the case of a rotation")
print("by 3, w, x, y and z would map to z, a, b and c. \n")

print("  Alphabet original: abcdefghijklmnopqrstuvwxyz")
print("Alphabet rotated +3: defghijklmnopqrstuvwxyzabc \n")

print("Example:")
print(" >     Text = 'Hello World!'")
print(" > Rotation = 4")
print(" > Solution = 'Lipps Asvph!' \n")


# Solution -------------------------------------------------------------

Text = "middle-Outz"
Rotation = 2

#Text = "Always-Look-on-the-Bright-Side-of-Life"
#Rotation = 5


Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w' ,'x',
            'y', 'z']

Rotation = Rotation%26

Alphabet_Rotated = Alphabet[Rotation: ] + Alphabet[ :Rotation]
Cisper = dict(zip(Alphabet, Alphabet_Rotated))


Message_In = list(Text)
Message_Out = ""

for letter in Message_In:

    Upper = letter.isupper()
    letter = letter.lower()

    if letter in Alphabet:
        new_letter = Cisper[letter]

    else:
        new_letter = letter


    if(Upper == True):
        new_letter = new_letter.upper()


    Message_Out = Message_Out + new_letter


print(f" > Solution = {Message_Out}")   

        
        

    





    

    

