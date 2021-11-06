
def BinarySearch(container, item, left_index, right_index):

    # Data NEED to be Sorted
    # The worst case is O(logN)

    # Base Case:
    if(left_index > right_index):
        return -1


    # Generate the index of the Middle Item:
    middle_index = (left_index + right_index) // 2


    # Item found!
    if(container[middle_index] == item):
       return middle_index
    

    # Checking the position of Middle Index
    elif(container[middle_index] > item):
        print(" > Checking items on the left...")
        return BinarySearch(container, item, left_index, middle_index-1)


    elif(container[middle_index] < item):
        print(" > Checking items on the right...")
        return BinarySearch(container, item, middle_index+1, right_index)


        
Nums = [ -4, 0, 1, 2, 9, 14, 25, 45, 49, 51, 60 ]


Finder = [-4, -2, 0, 1, 2, 3, 9, 14, 20, 25, 45, 46, 47, 50, 51, 60, 65, 70 ]

for find in Finder:
    pos = BinarySearch(Nums, find, 0, len(Nums)-1)
    print(f" > Num {find} is in the position {pos}. \n")
    
