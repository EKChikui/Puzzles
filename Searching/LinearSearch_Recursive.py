
def LinearSearch_Recursive(container, item, index= 0):

    # Base Case:

    # 1- When item is not present in the container.
    if(index >= len(container)):
       return -1


    # 2- When item is present in the container.
    if(container[index] == item):
       return index


    # Recursion

    return LinearSearch_Recursive(container, item, index= index+1)



Nums = [ 1, 4, 6, -4, 0, 55, 67, 89, 95, 100 ]

find = 67
print(LinearSearch_Recursive(Nums, find))
