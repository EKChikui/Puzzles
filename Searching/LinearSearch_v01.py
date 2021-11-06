
def LinearSearch(container, item):

    # The running time of this algorithm is O(n).
    # If data is unordered, use Linear Search.

    for index in range(0, len(container)):

        if container[index] == item:

            # Search Sucess!
            return index


    # Search Miss. Item not present 
    return -1


Nums = [ 1, 4, 5, -3, 10, 55, 100, 123 ]


find = 100
print(LinearSearch(Nums, find))

