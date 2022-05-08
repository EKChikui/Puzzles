
def Summation_Head(n):

    # Base Case: n=0
    if(n == 0):

        return 0


    # Recursion

    Sum = n + Summation_Head(n-1)
    return Sum


n = 1
while(n <= 20):

    get = Summation_Head(n)
    print(f"Sum({n}) = {get}")

    n = n+1
