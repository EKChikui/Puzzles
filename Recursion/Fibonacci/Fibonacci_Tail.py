
def Fibonacci_Tail(n, acc0= 0, acc1= 1):

    # Base-Case(s): F(0) = 0, F(1) = 1

    if(n == 0):
        return acc0

    if(n == 1):
        return acc1


    
    # Recursion

    return Fibonacci_Tail(n-1, acc1, acc1+acc0)



n = 0
while(n <= 10):

    get = Fibonacci_Tail(n)
    print(f"Fibonacci({n}) = {get}")

    n = n+1



