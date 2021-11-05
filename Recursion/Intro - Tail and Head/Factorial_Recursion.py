
def Factorial(n):

    # Tail Recursion

    # Base Case
    if(n == 1):
        return 1


    # Operation
    return n * Factorial(n-1)



get = Factorial(4)
print(get)
