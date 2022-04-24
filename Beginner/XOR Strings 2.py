
# XOR Strings 2

print("\n ****  XOR Strings 2  **** \n")

print("In this challenge, the task is to debug the existing code to successfully")
print("execute all provided test files. \n")

print("Given two strings consisting of digits 0 and 1 only, find the XOR of")
print("the two strings. \n")

print("Debug the given function strings_xor to find the XOR of the two given")
print("strings appropriately. \n")

print("Note: You can modify at most three lines in the given code and you")
print("      cannot add or remove lines to the code. \n")

print("The input consists of two lines. The first line of the input contains")
print("the first string, s , and the second line contains the second string, t. \n")


s = "01010"
t = "10101"

res = ""

for i in range(len(s)):

    if(s[i] == t[i]):
        res = res + "0";

    else:
        res = res + '1';


print(f" Solution: {res}")
