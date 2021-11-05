
def tail(n):

    print(f"Calling the function tail({n})")


    # Base Case
    if(n == 0):
        print("**** Base Case **** \n")
        return
    


    # Operation
    print(n)
    print("")


    # Recursive Function Call
    tail(n-1)


    # tail(5): -1006
    # RecursionError: maximum recursion depth exceeded while pickling
    #                 an object. (Stack Memory Overflow, if do not have
    #                 the base case "break".
    



tail(5)

# Answer:
#Calling the function tail(5)
#5
#
#Calling the function tail(4)
#4
#
#Calling the function tail(3)
#3
#
#Calling the function tail(2)
#2
#
#Calling the function tail(1)
#1
#
#Calling the function tail(0)
#**** Base Case ****
    
