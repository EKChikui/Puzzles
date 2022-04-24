
def Factorial_Head(n):

    # Base Case: 0! = 1

    if(n == 0):

        return 1


    # Recursion

    result1 = Factorial_Head(n-1)
    result2 = n * result1

    return result2



def Factorial_Tail(n, accumulator):

    # Base Case: 0! = 1
    if( n == 0):
        return accumulator


    # Recursion
    return Factorial_Tail(n-1, n*accumulator)


# n = 5

# 1st loop: n=5, accumulator=   1
# 2nd loop: n=4, accumulator=   5
# 3rd loop: n=3, accumulator=  20
# 4th loop: n=2, accumulator=  60
# 5th loop: n=1, accumulator= 120 (answer)


n = 5
head = Factorial_Head(n)
print(f"Factorial {n} using HEAD Recursion: {head}")

n = 6
tail = Factorial_Tail(n, 1)
print(f"Factorial {n} using TAIL Recursion: {tail}")
