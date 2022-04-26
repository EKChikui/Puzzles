
def Fibonacci_Head(n):

    # Base-Case(s): F(0) = 0, F(1) = 1
    if(n == 0):
        return 0

    if(n == 1):
        return 1


    # Recursion

    Fib1 = Fibonacci_Head(n-1)
    Fib2 = Fibonacci_Head(n-2)

    Result = Fib1 + Fib2

    return Result



n = 0
while(n <= 10):

    get = Fibonacci_Head(n)
    print(f" Fibonacci({n}) = {get}")

    n = n+1


# This solution has a problem for high numbers that will be solved with
# Dynamic Programming
