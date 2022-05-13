
def Summation_Tail(n, accumulator):

    # Base Case: n = 0
    if(n == 0):

        return accumulator


    # Recursion

    return Summation_Tail(n-1, n+accumulator)


n = 1
while(n <= 20):

    get = Summation_Tail(n, accumulator= 0)
    print(f"Sum({n}) = {get}")

    n = n+1

        
