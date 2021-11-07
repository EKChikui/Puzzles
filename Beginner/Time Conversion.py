
# Time Conversion

print("\n ****  Time Conversion  **** \n")

print("Given a time in -hour AM/PM format, convert it to military (24-hour)")
print("time. \n")

print("Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.")
print("      - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. \n")

print("Example:")
print("s = '12:01:00PM >> Return = '12:01:00'")
print("s = '12:01:00AM >> Return = '00:01:00' \n")



# Solution -------------------------------------------------------------

import math
import os
import random
import re
import sys


s = "07:05:45PM"
s = "12:01:34PM"


info = s[:]

is_pm = info.find("PM", 0)

if(is_pm >= 0):

    hour = info[0: info.find(":", 0)]
    hour = int(hour) + 12

    if(hour == 24):
        hour = 0

    print(hour)
