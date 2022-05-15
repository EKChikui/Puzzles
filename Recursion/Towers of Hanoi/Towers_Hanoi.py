
def Towers_Hanoi(disk, source, middle, destination):

    # Base Case:

    if(disk == 0):

        print(f"Disk {disk} from {source} to {destination}")
        return


    # Recursion:

    Towers_Hanoi(disk-1, source, destination, middle)
    # This is not necessarily the larget plate and also this is not
    # the plate 0 (Zero).

    print(f"Disk {disk} from {source} to {destination}")


    Towers_Hanoi(disk-1, middle, source, destination)
    print(f"Disk {disk} from {source} to {destination}")



Towers_Hanoi(2, "A", "B", "C")
print("")


