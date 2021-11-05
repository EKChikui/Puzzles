
def head(n):

    print(f"Calling the function head({n})")
    

    # Base Case
    if(n == 0):
        print("**** Base Case **** \n")
        return


    # Recursive Function Call
    head(n-1)


    # Operation
    print(n)


    # head(5): -1006
    # RecursionError: maximum recursion depth exceeded while pickling
    #                 an object. (Stack Memory Overflow, if do not have
    #                 the base case "break".



head(5)

# Answer:
#Calling the function head(5)
#Calling the function head(4)
#Calling the function head(3)
#Calling the function head(2)
#Calling the function head(1)
#Calling the function head(0)
#**** Base Case **** 
#
#1
#2
#3
#4
#5

