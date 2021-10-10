
# FizzBuzz

print("\n ****  FizzBuzz  **** \n")

print("Given a number n, for each integer in the range from 1 to n inclusive,")
print("print ine value per line as follows: \n")

print(" * If is a multiple of both 3 and 5, print FizzBuzz,")
print(" * If is only multiple of 3 (not 5) print Fizz,")
print(" * If is only multiple of 5 (not 3), print Buzz,")
print(" * If is not multiple of 3 and 5, print the value i. \n")


# Solution --------------------------------------------------------------

n = 31
print(f" > Given number = {n}")

for i in range(1, (n+1)):

    answer = ""

    if(i%3 == 0):
        answer = answer + "Fizz"

    if(i%5 == 0):
        answer = answer + "Buzz"

    if(answer == ""):
        answer = i


    print(answer)
